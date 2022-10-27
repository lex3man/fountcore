from django.contrib import admin
from apps.sites.models import Item, Site, IslandType, Island

class ItemAdmin(admin.ModelAdmin):
    list_display = ('caption', 'identity', 'description', 'site')
    search_fields = ('caption', 'description')
    list_filter = ('site',)

class SiteAdim(admin.ModelAdmin):
    list_display = ('caption', 'domain')

class IslandAdmin(admin.ModelAdmin):
    list_display = ('caption', 'identity', 'type')

admin.site.register(Item, ItemAdmin)
admin.site.register(Site, SiteAdim)
admin.site.register(Island, IslandAdmin)
admin.site.register(IslandType)