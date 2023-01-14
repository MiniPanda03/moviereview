from rest_framework import serializers
from rest_framework.response import Response
from .models import Actor, Director, Movie, Rating
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


UserModel = get_user_model()

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'Name','Surname']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'Name','Surname']

class MovieSerializer(serializers.ModelSerializer):
    Actor_id = ActorSerializer(many=True)
    Director_id = DirectorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id','Title','Description','Slug','Director_id','Actor_id','created','updated']


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user


    class Meta:
        model = User
        fields = ('id', 'username','password')


class RatingSerializer(serializers.ModelSerializer):
    movie_id = MovieSerializer(many=False)
    user_id = UserSerializer(many=False)
    class Meta:
        model = Rating
        fields = ['id','movie_id','user_id','ratingValue']