from flask_restx import Api
from flask import Blueprint

from .user.controller import api as user_ns
from .movie.controller import api as movie_ns
from .genre.controller import api as genre_ns

# Import controller APIs as namespaces.
api_bp = Blueprint("api", __name__)

api = Api(api_bp, title="API", description="Main routes.")

# API namespaces
api.add_namespace(user_ns)
api.add_namespace(movie_ns)
api.add_namespace(genre_ns)
