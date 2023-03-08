from django.contrib import admin
from . import models


@admin.register(models.SpaceShip)
class SpaceShipAdmin(admin.ModelAdmin):
    list_display = ['name', 'nickname', 'classification', 'engine_type']
    list_per_page = 10
    search_fields = ['first_name__istartswith', 'classification__istartswith']


@admin.register(models.Crew)
class CrewAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'nickname', 'origin', 'staff_level']
    list_editable = ['staff_level']
    list_per_page = 10
    ordering = ['first_name', 'last_name', 'origin', 'staff_level']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
