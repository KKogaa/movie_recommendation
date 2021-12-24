from app.models.schemas import GenreSchema
from app.models.genre import Genre
from app.utils import message, err_resp, internal_err_resp

from app import db
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import GenreService
from .dto import GenreDto

api = GenreDto.api
data_resp = GenreDto.data_resp


@api.route("")
class Genre(Resource):
    # @api.doc(
    #     "Get a specific user",
    #     responses={
    #         200: ("User data successfully sent", data_resp),
    #         404: "User not found!",
    #     },
    # )
    def get(self):
        """ Get a specific user's data by their username """
        return GenreService.get_all_genres()

    # @api.expect(auth_register, validate=True)
    def post(self):
        """ User registration """
        # Grab the json data
        register_data = request.get_json()

        # Validate data
        # if (errors := register_schema.validate(register_data)) :
        #     return validation_error(False, errors), 400

        return GenreService.save_genre(register_data)


@api.route("/<int:genre_id>")
class GenreId(Resource):

    # get specific genre data
    @api.doc(
        "Get a specific genre",
        responses={
            200: ("Genre data successfully sent", data_resp),
            404: "Genre not found!",
        },
    )
    def get(self, genre_id):
        return GenreService.get_genre(genre_id)

    # delte a specific genre
    def delete(self, genre_id):
        return GenreService.delete_genre(genre_id)

    # update a specific genre
    def put(self, genre_id):
        # Grab the json data
        update_data = request.get_json()

        # Validate data
        # if (errors := register_schema.validate(update_data)) :
        #     return validation_error(False, errors), 400

        return GenreService.update_genre(genre_id, update_data)
