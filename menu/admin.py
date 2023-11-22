from django.contrib import admin

from menu.models import Menu


# Register your models here.


@admin.register(Menu)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'previous_tab', )
    list_filter = ('name', )
    search_fields = ('name', )
