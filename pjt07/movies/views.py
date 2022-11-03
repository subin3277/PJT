
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import *


# Create your views here.
@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializers = ActorListSerializer(actors, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    serializers = ActorSerializer(actor)
    return Response(serializers.data)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializers = MovieListSerializer(movies, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    serializers = MovieSerializer(movie)
    return Response(serializers.data)

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializers = ReviewListSerializer(reviews, many=True)
    return Response(serializers.data)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, movie_pk):
    review = Review.objects.get(pk=movie_pk)
    if request.method == 'GET':
        serializers = ReviewSerializer(review)
        return Response(serializers.data)
    elif request.method == 'PUT':
        serializers = ReviewSerializer(review, data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializers = ReviewSerializer(data=request.data)
    if serializers.is_valid(raise_exception=True):
        serializers.save(movie=movie)
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST)