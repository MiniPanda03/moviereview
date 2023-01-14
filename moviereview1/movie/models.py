from django.db import models

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
    Name =  models.CharField(max_length=255)
    Description = models.CharField(max_length=500)
    Slug = models.SlugField(max_length=40)
    Director_id = models.ManyToManyField(Director)
    Actor_id = models.ManyToManyField(Actor)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __str__(self):
        return self.Name


    def get_actors(self):
        return ",".join([str(p) for p in self.Actor_id.all()])

    def get_directors(self):
        return ",".join([str(p) for p in self.Director_id.all()])




class Rating(models.Model):
    ratingValue = models.IntegerField()
    user_id = models.IntegerField()
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return "{} : {}".format(self.movie_id,self.user_id)
