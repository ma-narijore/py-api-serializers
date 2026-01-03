from rest_framework import viewsets

from cinema.models import Genre, Actor, Movie
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    MovieListSerializer,
        MovieDetailSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieListSerializer

    def get_queryset(self):
         return Movie.objects.prefetch_related("actors", "genres")

