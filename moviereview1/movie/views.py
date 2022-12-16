from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Actor

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