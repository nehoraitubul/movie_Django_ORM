import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"

django.setup()

from movies_app.models import *

m = Movie.objects.get(id=3)
# new_actor = Actor(name='ttt', birth_year=2020)
# new_actor.save()
# ma= MovieActor(movie=m, actor=new_actor, salary=100000, main_role=False)
# ma.save()

# new_actor = Actor.objects.create(name='ppp', birth_year=2014)
# ma= MovieActor(movie_id=m.id, actor_id=new_actor.id, salary=100000, main_role=False)
# ma.save()

# m.actors.create(name='yyy', birth_year=2001, through_defaults={'salary': 200000, 'main_role': True})


# m = Movie.objects.get(id=1)
# m.actor.add(Actor.objects.get(id=2), through_defaults={'salary': 300000, 'main_role': True})


# m = Movie.objects.get(id=3)
# a = Actor.objects.get(name__contains='ttt')
# m.actors.remove(a)


m = Movie.objects.get(id=3)
print(m.actors.all())
print(m.movieactor.all())

a = Actor.objects.get(id=3)
print(a.movie_set.all())
a.movie_set.add(Actor.objects.get(id=2), through_defaults={'salary': 400000, 'main_role': False})