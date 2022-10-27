from django.contrib import admin
from .models import User, TelegramAsset

@admin.register(TelegramAsset)
class TelegAdmin(admin.ModelAdmin):
    list_display = ('fname', 'username', 'tid', 'on_fox', 'from_bot')
    readonly_fields = ('on_fox', 'tid', 'from_bot')
    search_fields = ('fname', 'lname', 'username', 'tid')
    list_filter = ('on_fox', 'from_bot')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'uid', 'status')
    readonly_fields = ('uid',)
    list_filter = ('status',)
    search_fields = ('name', 'uid')