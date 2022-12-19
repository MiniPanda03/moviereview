from django.db import models

class Actor (models.Model):
    Name = models.CharField(max_length=255)
    Surname = models.CharField(max_length=255)


class Director (models.Model):
    Name = models.CharField(max_length=255)
    Surname = models.CharField(max_length=255)

class Movie (models.Model):
    Name =  models.CharField(max_length=255)
    Description = models.CharField(max_length=500)
    Slug = models.SlugField(max_length=40)
    Director_id = models.ManyToManyField(Director)
    Actor_id = models.ManyToManyField(Actor)
    created = models.DateTimeField()
    updated = models.DateTimeField()



class Raiting(models.Model):
    raitingValue = models.IntegerField()
    user_id = models.IntegerField()
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)
