from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from django.template import loader
from django.urls import reverse
from rest_framework import status as stat
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

def create(request):
    return 0

def update(request):
    return 0

def get_all_movies(request):
    movie = Movie.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'Movie': movie,
    }
    return HttpResponse(template.render(context, request))

def filter_by_title(request):
    mydata = Movie.objects.filter(Movie_Title='')
    template = loader.get_template('index.html')
    context = {
        'Movies': mydata,
    }
    return HttpResponse(template.render(context, request))

def get_by_title(request):
    mydata = Movie.objects.values_list('firstname')
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

def order_by_mean_rating(request):
    return 0

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def create(self, request, *args, **kwargs):
        try:
            name = request.data.get('Name')
            surname = request.data.get('Surname')
            actor = Actor.objects.create(Name=name,Surname=surname)
            serializer = ActorSerializer(actor, many=False)
            response = {'Yay': 'Aktor dodany', 'Wynik': serializer.data}
            return Response(response,status=stat.HTTP_201_CREATED)
        except:
            response = {'Ups': 'Coś poszło nie tak'}
            return Response(response, status=stat.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        try:
            actor_object = Actor.objects.get(id=pk)
            actor_data = request.data
            actor_object.name = actor_data.get('name')
            actor_object.surname = actor_data.get('surname')

            actor_object.save()
            serializers = ActorSerializer(actor_object, many=False)
            response = {'Yay': 'Update udany', 'Wynik': serializers.data}
            return Response(response, status=stat.HTTP_200_OK)
        except:
            response = {'Ups': 'Coś poszło nie tak'}
            return Response(response, status=stat.HTTP_400_BAD_REQUEST)


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def create(self, request, *args, **kwargs):
        try:
            name = request.data.get('Name')
            surname = request.data.get('Surname')
            director = Director.objects.create(Name=name,Surname=surname)
            serializer = ActorSerializer(director, many=False)
            response = {'Yay': 'Reżyser dodany', 'Wynik': serializer.data}
            return Response(response,status=stat.HTTP_201_CREATED)
        except:
            response = {'Ups': 'Coś poszło nie tak'}
            return Response(response, status=stat.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        try:
            diector_object = Director.objects.get(id=pk)
            director_data = request.data
            diector_object.name = director_data.get('name')
            diector_object.surname = director_data.get('surname')

            diector_object.save()
            serializers = DirectorSerializer(diector_object, many=False)
            response = {'Yay': 'Update udany', 'Wynik': serializers.data}
            return Response(response, status=stat.HTTP_200_OK)
        except:
            response = {'Ups': 'Coś poszło nie tak'}
            return Response(response, status=stat.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer