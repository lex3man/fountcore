from django.contrib import admin
from apps.environment.models import GlobalSetting, Variables

class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

class VariablesAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    search_fields = ('name', 'value')

admin.site.register(GlobalSetting, SettingsAdmin)
admin.site.register(Variables, VariablesAdmin)