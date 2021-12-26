from flask import current_app

from app import db
from app.utils import err_resp, message, internal_err_resp
from app.models.movie import Movie
from app.models.genre import Genre
import pandas as pd

from app.models.schemas import MovieSchema
movie_schema = MovieSchema()


class MovieService:
    @staticmethod
    def get_all_movies():
        """ Get all moviews """
        if not (movies := Movie.query.all()):
            return err_resp("User not found!", "user_404", 404)

        from .utils import load_datas

        try:
            movie_data = load_datas(movies)

            resp = message(True, "Movies data sent")
            resp["movies"] = movie_data
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def save_movie(data):
        # Required values
        title = data["title"]
        genres = data.get("genres")

        try:
            new_movie = Movie(
                title=title
            )
            for id_genre in genres:
                if obj := Genre.query.filter_by(id=id_genre).first():
                    new_movie.genres.append(obj)

            db.session.add(new_movie)
            db.session.flush()

            # Load the new movie info
            movie_info = movie_schema.dump(new_movie)

            # Commit changes to DB
            db.session.commit()

            resp = message(True, "Movie has successfully been created")
            resp["movie"] = movie_info

            return resp, 201

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def get_movie(movie_id):
        if not (movie := Movie.query.get(movie_id)):
            return err_resp("Movie not found!", "movie_404", 404)

        from .utils import load_data

        try:
            movie_info = load_data(movie)

            resp = message(True, "Movie data sent")
            resp["movie"] = movie_info
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def update_movie(movie_id, data):
        if not (movie := Movie.query.get(movie_id)):
            return err_resp("Movie not found!", "movie_404", 404)

        # Required values
        title = data["title"]

        try:
            movie.title = title

            db.session.add(movie)
            db.session.flush()

            # Load the new movie info
            movie_info = movie_schema.dump(movie)

            # Commit changes to DB
            db.session.commit()

            resp = message(True, "Movie has successfully been updated")
            resp["movie"] = movie_info

            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def delete_movie(movie_id):
        if not (movie := Movie.query.get(movie_id)):
            return err_resp("Movie not found!", "movie_404", 404)

        try:
            db.session.delete(movie)
            db.session.flush()
            db.session.commit()

            resp = message(True, "Movie has successfully been deleted")
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def process_file(file):
        print('Entro')
        print(file.filename)

        try:

            # data = file.read().decode("utf-8")
            # return data
            return None

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
