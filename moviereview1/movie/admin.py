from django.contrib import admin
from .models import Actor,Movie,Director, Rating


class ActorAdmin(admin.ModelAdmin):
    fields = ['Name', 'Surname']
    search_fields = ['Name']
    list_display = ['Name', 'Surname']
    list_filter = ['Name']


class DirectorAdmin(admin.ModelAdmin):
    fields = ['Name', 'Surname']
    list_display = ['Name', 'Surname']
    list_filter = ['Surname']



class MovieAdmin(admin.ModelAdmin):
    fields = ['Title','Description','Slug','get_directors','get_actors','created','updated']
    list_display = ['Title','Description','Slug','get_directors','get_actors','created','updated']
    prepopulated_fields = {"Slug": ("Title",)}
    list_filter = ['Title']

class RatingAdmin(admin.ModelAdmin):
    fields = ['movie_id','user_id','ratingValue']
    list_display = ['id','movie_id','user_id','ratingValue']


admin.site.register(Actor,ActorAdmin)
admin.site.register(Director,DirectorAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Rating,RatingAdmin)