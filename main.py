import os
import django
import datetime

from django.db.models import Q, Count, Min, Max

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"

django.setup()

from movies_app.models import *

# new_movie = Movie(name="bbb", duration_in_min=124, release_tear=2020)
# new_movie.save()

# all_movies = Movie.objects.all()
# total_duration = 0
# for m in all_movies:
#     total_duration += m.duration_in_min
# print(total_duration)


# all_movies = Movie.objects.all()
# for m in all_movies:
#     Rating(movie=m, rating=9).save()





#----------- TESTS ------------
# movie = Movie.objects.get(pk=3)
# print(movie.rating_set.all())

# r = Rating.objects.get(pk=1)
# print(r.movie_id)
# print(r.movie)

# movie = Movie.objects.get(pk=3)
# print(movie.rating_set.all())

# m = Movie.objects.all().values_list('name', 'release_tear')
# print(m)
#
# m = m.filter(release_tear__gt=2015)
# print(m)

# filter_by_year, filter_by_num = 2020, None
# m = Movie.objects.all()
# if filter_by_year:
#     m = m.filter(release_tear=filter_by_num)


#---W4.1---
def get_actor_by_age(age):
    actor = Actor.objects.all()
    age = datetime.datetime.today().year - age
    actor = actor.filter(birth_year__gte=age)
    print(actor)


#---W4.2---
def get_movie_by_time_and_date(minuets, year):
    movies = Movie.objects.all()
    movies = movies.filter(duration_in_min__gte=minuets, release_year__gt=year)
    print(movies)

#---W4.3---
def get_w4_3():
    movies = Movie.objects.all()
    movies = movies.filter(Q(description__icontains='mob') | Q(description__icontains='cob') | Q(description__icontains='criminal'))
    print(movies)

#---W4.4---
def get_w4_4():
    print(Movie.objects.filter(Q(description__icontains='mob') | Q(description__icontains='cob') | Q(description__icontains='criminal'), release_year__lt=2010))

#---W4.5---
def get_w4_5():
    actors = Actor.objects.annotate(Count('movieactor'))
    for i in actors:
        print(i, i.movieactor__count)

#---W4.6---
def get_w4_6():
    all_actors = Actor.objects.annotate(min_rating=Min('movie__rating__rating'), max_rating=Max('movie__rating__rating'))
    for i in all_actors:
        print(i.name, i.min_rating, i.max_rating)

if __name__ == '__main__':
    # get_actor_by_age(50)
    # get_movie_by_time_and_date(150, 2005)
    # get_w4_3()
    # get_w4_4()
    # get_w4_5()
    get_w4_6()