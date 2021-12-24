from flask import current_app

from app import db
from app.utils import err_resp, message, internal_err_resp
from app.models.movie import Movie

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
        # Assign vars

        # Required values
        title = data["title"]
        genres = data["genres"]
        print(genres)

        try:
            new_movie = Movie(
                title=title
                # genres=genres
            )

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
