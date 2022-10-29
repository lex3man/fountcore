from django.db import models
from apps.bots.models import Bot

STATUSES = [
    ('usr','Пользователь'),
    ('stf','Персонал'),
    ('adm','Администратор'),
    ('own','Владыка'),
]

class TelegramAsset(models.Model):
    tid = models.CharField(verbose_name="ID", max_length=20)
    username = models.CharField(verbose_name="Имя пользователя", max_length=150, null=True)
    fname = models.CharField(verbose_name="Имя", max_length=150, null=True)
    lname = models.CharField(verbose_name="Фамилия", max_length=150, null=True)
    on_fox = models.BooleanField(verbose_name="Слушает", default=True)
    from_bot = models.ForeignKey(Bot, verbose_name="Через бота", on_delete=models.SET_NULL, null=True)
    state_id = models.CharField(verbose_name="Стадия", max_length=50, null=True, blank=True)#, editable=False)

    def __str__(self):
        return f'{self.tid} ({self.fname})'
    

class User(models.Model):
    uid = models.CharField(verbose_name="ID пользователя", max_length=11, unique=True)
    name = models.CharField(verbose_name="Имя пользователя", max_length=50)
    status = models.CharField(verbose_name="Статус", max_length=3, choices = STATUSES, default="usr")
    telegram = models.ForeignKey(TelegramAsset, verbose_name='Телеграм', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['uid', 'name']
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    
    def __str__(self):
        return self.name
    
