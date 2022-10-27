from django.contrib import admin
from .models import Bot, State, Button, Keyboard, ContentBlock, Log, Command

admin.site.register(State)

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('bot', 'event_type', 'time')
    list_filter = ('bot',)
    search_fields = ('details',)

@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ('caption', 'bot_type', 'description', 'active')
    readonly_fields = ('active', 'bot_id')
    list_filter = ('bot_type', 'active')
    search_fields = ('caption', 'description', 'bot_id')
    actions = [Bot.Start, Bot.Stop]

@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = ('caption', 'callback', 'lang')
    list_filter = ('lang',)

@admin.register(Keyboard)
class KeyboardAdmin(admin.ModelAdmin):
    list_display = ('caption', 'kb_type', 'lang')
    list_filter = ('lang',)

@admin.register(ContentBlock)
class CBAdmin(admin.ModelAdmin):
    list_display = ('caption', 'content', 'state', 'keyboard')
    list_filter = ('lang', 'state')
    search_fields = ('caption', 'content')

@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'bot')
    list_filter = ('bot',)