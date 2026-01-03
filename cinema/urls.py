from django.urls import path, include
from rest_framework import routers

from cinema import views

router = routers.DefaultRouter()
router.register(r'genres', views.GenreViewSet, basename="genre")
router.register(r'actors', views.ActorViewSet, basename="actor")
router.register(r"movies", views.MovieViewSet, basename="movie")

urlpatterns = [
    path("", include(router.urls)),
]
