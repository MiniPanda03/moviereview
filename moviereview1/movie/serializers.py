from rest_framework import serializers
from .models import Actor, Director

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id','name','surname']


class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ['id','name','surname']