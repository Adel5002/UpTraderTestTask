from django.contrib import admin
from .models import Menu, MenuItem, MenuItemChild


class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class MenuItemChildAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('text',)}


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem)
admin.site.register(MenuItemChild, MenuItemChildAdmin)
