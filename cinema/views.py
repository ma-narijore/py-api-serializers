from rest_framework import viewsets

from cinema.models import Genre, Actor, Movie, CinemaHall, MovieSession
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    CinemaHallSerializer,
    MovieSessionSerializer,
    MovieSessionDetailSerializer
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieListSerializer

    def get_queryset(self):
         return Movie.objects.prefetch_related("actors", "genres")


class MovieSessionViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
         return MovieSession.objects.select_related("movie", "cinema_hall")

    def get_serializer_class(self):
        if self.action == "retrieve":  # detail view
            return MovieSessionDetailSerializer
        return MovieSessionSerializer
