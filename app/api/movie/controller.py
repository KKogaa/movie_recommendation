from app.models.schemas import MovieSchema
from app.models.movie import Movie
from app.utils import message, err_resp, internal_err_resp

from app import db
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import MovieService
from .dto import MovieDto

api = MovieDto.api
data_resp = MovieDto.data_resp


@api.route("")
class Movie(Resource):
    @api.doc(
        "Get a specific user",
        responses={
            200: ("Movie data successfully sent", data_resp),
            404: "Movie not found!",
        },
    )
    def get(self):
        """ Get a specific user's data by their username """
        return MovieService.get_all_movies()

    # @api.expect(auth_register, validate=True)
    def post(self):
        """ User registration """
        # Grab the json data
        register_data = request.get_json()

        # Validate data
        # if (errors := register_schema.validate(register_data)) :
        #     return validation_error(False, errors), 400

        return MovieService.save_movie(register_data)
