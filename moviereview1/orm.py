from django.db.models import Avg

from movie.models import Actor,Rating,Director,Movie
from django.contrib.auth.models import User


#Create
user = User.objects.create_user(username="Test1", email="test1@yup.com",password="Qwerty123!")

actor = Actor.objects.create(Name="aaaaa",Surname="bbbbbbbb")

director = Director.objects.create(Name="aaaaa",Surname="bbbbbbbb")

movie = Movie.objects.create(Title='Yup2',Description='ASsdffdfd',Slug='/yup2')
movie.Actor_id.add(actor)
movie.Director_id.add(director)

rating = Rating.objects.create(ratingValue=3,user_id=user,movie_id=movie)

#Update
movie.Title = "yup2"
movie.save()

rating.ratingValue = 1
rating.save()

# All

Movie.objects.all()

# filter
Movie.objects.filter(Title__startswith='Y')

# get
Movie.objects.get(Title="Yup")

#order by
Rating.objects.select_related('movie_id').values('movie_id').annotate(Avg('ratingValue')).order_by('ratingValue')
