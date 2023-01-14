from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Actor, Director
from rest_framework import viewsets
from .serializers import DirectorSerializer, ActorSerializer

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