from django.contrib import admin
from .models import Actor,Movie,Director


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ['Name']
    list_display = ['id', 'Name', 'Surname']
    list_filter = ['Name']


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Surname']
    list_filter = ['Surname']