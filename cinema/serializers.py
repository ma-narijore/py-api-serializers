from rest_framework import serializers

from cinema.models import (
    Genre,
    Actor,
    Movie,
)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name",)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name",)


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )
    # Accept actor IDs for POST, display names for GET
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors",)

    def get_queryset(self):
        queryset = Movie.objects.all()
        if self.action == "list":
            queryset = queryset.prefetch_related("genres", "actors")

        elif self.action == "retrieve":
            queryset = queryset.prefetch_related("genres", "actors")

    def get_actors(self, obj):
        return [f"{actor.first_name} {actor.last_name}" for actor in obj.actors.all()]

    def to_representation(self, instance):
        """Customize output: display names for list view"""
        rep = super().to_representation(instance)
        rep["genres"] = [genre.name for genre in instance.genres.all()]
        rep["actors"] = [f"{a.first_name} {a.last_name}" for a in instance.actors.all()]
        return rep


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")
