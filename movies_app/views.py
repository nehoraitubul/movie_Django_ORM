import datetime

from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movies_app.models import *
from . import serializers


def get_movies_list(request):
    movies_qs = Movie.objects.all()
    if 'name' in request.query_params:
        movies_qs = movies_qs.filter(name__iexact=request.query_params['name'])
    if 'duration_from' in request.query_params:
        movies_qs = movies_qs.filter(duration_in_min__gte=request.query_params['duration_from'])
    if 'duration_to' in request.query_params:
        movies_qs = movies_qs.filter(duration_in_min__lte=request.query_params['duration_to'])
    if 'description' in request.query_params:
        movies_qs = movies_qs.filter(description__icontains=request.query_params['description'])

    if not movies_qs:
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = serializers.MovieSerializer(movies_qs, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        return get_movies_list(request)
    elif request.method == 'POST':
        serializer = serializers.MovieDetailsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.validated_data
            serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)



def delete_movie(request, movie_id: int):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH', 'DELETE'])
def get_movie_details(request, movie_id: int):
    # try:

    #     movie = Movie.objects.get(id=movie_id)

    #----------------------------------------------------------------------
    #     #-- NOT WORKING --
    #     # if not movie:
    #     #     return Response(status=status.HTTP_404_NOT_FOUND)
    # ----------------------------------------------------------------------

    #     serializer = serializers.MovieDetailsSerializer(movie, many=False)
    #     return Response(serializer.data)

    # except Movie.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'GET':
        serializer = serializers.MovieDetailsSerializer(movie, many=False)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = serializers.MovieDetailsSerializer(movie, data=request.data, many=False, partial=True) # partial = all the required params in seri, set them to not req
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response()
    elif request.method == 'DELETE':
        return delete_movie(request, movie_id)




@api_view(['GET'])
def get_ratings(requests):
    rating = Rating.objects.all()
    if 'date' in requests.query_params:
        date = requests.query_params['date']
        print(date)
        rating = rating.filter(rating_date=datetime.datetime.strptime(date, '%Y-%m-%d'))
    if 'year' in requests.query_params:
        rating = rating.filter(rating_date__year=requests.query_params['year'])
    if 'month' in requests.query_params:
        rating = rating.filter(rating_date__month=requests.query_params['month'])
    if 'day' in requests.query_params:
        rating = rating.filter(rating_date__day=requests.query_params['day'])

    if not rating:
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = serializers.RatingGetDetails(rating, many=True)
    return Response(serializer.data)




@api_view(['GET', 'POST'])
def movie_actors(requests, movie_id):

    if requests.method == 'GET':
        movie_actors = MovieActor.objects.filter(movie_id=movie_id)
        serializer = serializers.MovieActorSerializer(movie_actors, many=True)
        return Response(serializer.data)

    elif requests.method == 'POST':
        get_object_or_404(Movie ,id=movie_id)
        serializer = serializers.AddMovieActorSerializer(data=requests.data, context={'movie_id': movie_id, 'request':requests})
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response()

