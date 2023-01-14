from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models import signals


class Actor (models.Model):
    Name = models.CharField(max_length=255)
    Surname = models.CharField(max_length=255)


    def __str__(self):
        return "{} {}".format(self.Name,self.Surname)

class Director (models.Model):
    Name = models.CharField(max_length=255)
    Surname = models.CharField(max_length=255)

    def __str__(self):
        return "{} {}".format(self.Name,self.Surname)

class Movie (models.Model):
    Title =  models.CharField(max_length=255)
    Description = models.CharField(max_length=500)
    Slug = models.SlugField(max_length=40)
    Director_id = models.ManyToManyField(Director)
    Actor_id = models.ManyToManyField(Actor)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title


    def get_actors(self):
        return ",".join([str(p) for p in self.Actor_id.all()])

    def get_directors(self):
        return ",".join([str(p) for p in self.Director_id.all()])

@receiver(signals.pre_save, sender=Movie)
def populate_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.Title)


class Rating(models.Model):
    ratingValue = models.IntegerField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return "{} : {}".format(self.movie_id,self.user_id)
