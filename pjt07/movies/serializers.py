from pyexpat import model
from rest_framework import serializers
from movies.models import *

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview')



class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content')

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        
class MovieSerializer(serializers.ModelSerializer):
    actors = ActorListSerializer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'