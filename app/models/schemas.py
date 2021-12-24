# Model Schemas
from app import ma

from .user import User
from .genre import Genre
from .movie import Movie


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("email", "name", "username", "joined_date", "role_id")


class GenreSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "description",)


class MovieSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "title", "genres")
    genres = ma.Nested(GenreSchema, many=True)
