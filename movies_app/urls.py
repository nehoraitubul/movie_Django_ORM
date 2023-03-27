from django.urls import path

from . import views

urlpatterns = [
    path('api/movies', views.movie_list),
    path('api/movies/<int:movie_id>', views.get_movie_details),
    path('api/rating', views.get_ratings),
    path('api/movies/<int:movie_id>/actors', views.movie_actors),
    path('static', views.my_host),
]