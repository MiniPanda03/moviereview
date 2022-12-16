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
    Director_id = models.ForeignKey(Director,null=True,on_delete=models.SET_NULL)
    Avg_raiting = models.DecimalField(max_digits=5,decimal_places=2)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    raitingAmount = models.IntegerField()



class Actors (models.Model):
    Movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)
    Actor_id = models.ForeignKey(Actor,on_delete=models.CASCADE)

class Raiting(models.Model):
    raitingValue = models.IntegerField()
    user_id = models.IntegerField()
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)
