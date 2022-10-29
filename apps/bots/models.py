from django.db import models
from django.contrib import admin
import subprocess, os, redis, signal

active_bots = {}
bots_status = redis.Redis(db=5, host='redis')
bot_processes = redis.Redis(db=4, host='redis')
controller_script = '/app/bot_handler/start.py'

STATE_MODES = [
    ('wfb', 'Ожидание нажатия кнопки'),
    ('inp', 'Ожидание ввода'),
]

BOT_TYPES = [
    ('TG', 'Telegram bot'),
]

EVENT_TYPES = [
    ('start', 'Начало работы'),
    ('update', 'Изменение'),
    ('stop', 'Остановлен'),
]

KEYBOARD_TYPES = [
    ('std', 'Стандартная'),
    ('inl', 'Inline'),
]

LANGUEGES = [
    ('RUS', 'Русский'),
    ('ENG', 'English'),
]

class Button(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=150, unique=True)
    lang = models.CharField(verbose_name="Язык", max_length=10, default="RUS", choices = LANGUEGES)
    callback = models.CharField(verbose_name="Callback", max_length=50, null=True, blank=True)
    row = models.IntegerField(verbose_name="Ряд", default=1)

    class Meta:
        verbose_name = 'Кнопка'
        verbose_name_plural = 'Кнопки'
    
    def __str__(self):
        return self.caption

class Keyboard(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=150, unique=True)
    lang = models.CharField(verbose_name="Язык", max_length=10, default="RUS", choices = LANGUEGES)
    kb_type = models.CharField(verbose_name="Тип клавиатуры", max_length=10, choices = KEYBOARD_TYPES)
    buttons = models.ManyToManyField(Button, verbose_name="Кнопки клавиатуры")

    class Meta:
        verbose_name = 'Клавиатура'
        verbose_name_plural = 'Клавиатуры'

    def __str__(self):
        return self.caption

class Bot(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=150, unique=True)
    bot_type = models.CharField(verbose_name="Тип бота", choices=BOT_TYPES, default='TG', max_length=10)
    bot_id = models.CharField(verbose_name="ID бота", max_length=50, null=True, blank=True)
    active = models.BooleanField(verbose_name="Активен", default=False)
    token = models.CharField(verbose_name="Токен", max_length=150)
    description = models.TextField(verbose_name="Описание", null=True)

    def __str__(self):
        return self.caption

    # class Meta:
        # verbose_name = 'Бот'
        # verbose_name_plural = 'Боты'

    @admin.action(description = 'Запустить выбранных ботов')
    def Start(self, _, queryset):
        for bot in queryset:
            if bot.active == False:
                process = subprocess.Popen(['python', controller_script, bot.token])
                bot_processes.mset({bot.caption:process.pid})
                bot.active = True
                bot.save()
                
    @admin.action(description = 'Остановить выбранных ботов')
    def Stop(self, _, queryset):
        for bot in queryset:
            if bot.active == True:
                try:
                    process = bot_processes.get(bot.caption)
                    os.kill(int(process), signal.SIGKILL)
                    bot_processes.mset({bot.caption:'None'})
                except: pass
                bot.active = False
                bot.save()
                log = Log(bot = bot, event_type = 'stop', details = '')
                log.save()

class Log(models.Model):
    bot = models.ForeignKey(Bot, verbose_name="Бот", on_delete=models.SET_NULL, null=True)
    event_type = models.CharField(verbose_name="Тип события", max_length=10, choices = EVENT_TYPES)
    time = models.DateTimeField(verbose_name="Время", auto_now=False, auto_now_add=True)
    details = models.TextField(verbose_name="Дополнительно", null=True, blank=True)

    def __str__(self):
        return f'{self.event_type} {self.bot}'
    
class State(models.Model):
    sid = models.CharField(verbose_name="ID", max_length=11, unique=True)
    caption = models.CharField(verbose_name="Наименование", max_length=150, unique=True)
    mode = models.CharField(verbose_name="Режим", max_length=10, choices=STATE_MODES, default='wfb')

    def __str__(self):
        return self.caption

class ContentBlock(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=150, unique=True)
    lang = models.CharField(verbose_name="Язык", max_length=10, default="RUS", choices = LANGUEGES)
    bot = models.ForeignKey(Bot, verbose_name="Бот", on_delete=models.SET_NULL, null=True)
    content = models.TextField(verbose_name="Текст", null=True, blank=True)
    keyboard = models.ForeignKey(Keyboard, verbose_name="Клавиатура", on_delete=models.SET_NULL, null=True, blank=True)
    next_state = models.ForeignKey(State, related_name="next", verbose_name="Новый стэйт", on_delete=models.SET_NULL, null=True, blank=True)
    prev_state = models.ForeignKey(State, related_name="previos", verbose_name="Предыдущий стэйт", on_delete=models.SET_NULL, null=True, blank=True)
    from_button = models.ForeignKey(Button, verbose_name="По кнопке", on_delete=models.SET_NULL, null=True, blank=True)
    next_block = models.ForeignKey("self", verbose_name="Следующий блок", on_delete=models.SET_NULL, null=True, blank=True)
    delay = models.IntegerField(verbose_name="Задержка перед ответом (в сек)", default=0)

    class Meta:
        verbose_name = "Блок контента"
        verbose_name_plural = "Блоки контента"

    def __str__(self):
        return self.caption

class Command(models.Model):
    keyword = models.CharField(verbose_name="Команда", max_length=50)
    bot = models.ForeignKey(Bot, verbose_name="Бот", on_delete=models.SET_NULL, null=True)
    answer = models.TextField(verbose_name="Текст ответа", null=True, blank=True)
    keyboard = models.ForeignKey(Keyboard, verbose_name="Клавиатура", on_delete=models.SET_NULL, null=True, blank=True)
    next_block = models.ForeignKey("self", verbose_name="Следующий блок", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"
        ordering = ['keyword']
    
    def __str__(self):
        return self.keyword
    
