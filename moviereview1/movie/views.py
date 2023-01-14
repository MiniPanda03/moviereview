from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Actor, Director,Movie,Rating
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import DirectorSerializer, ActorSerializer,UserSerializer,MovieSerializer,RatingSerializer

def index(request):
    actor = Actor.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'actors': actor,
    }
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  name = request.POST['name']
  surname = request.POST['surname']
  member = Actor(Name=name, Surname=surname)
  member.save()
  return HttpResponseRedirect(reverse('index'))


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer