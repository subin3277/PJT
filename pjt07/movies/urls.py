
from django.urls import path, include
from movies import views

urlpatterns = [
    path('actors/', views.actor_list),
    path('actors/<int:actor_pk>/', views.actor_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('reviews/', views.review_list),
    path('reviews/<int:movie_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/reviews/', views.create_review),
]