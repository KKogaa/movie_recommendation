from flask import current_app

from app import db
from app.utils import err_resp, message, internal_err_resp
from app.models.genre import Genre

from app.models.schemas import GenreSchema

genre_schema = GenreSchema()


class GenreService:
    @staticmethod
    def get_all_genres():
        """ Get all moviews """
        if not (genres := Genre.query.all()):
            return err_resp("Genre not found!", "user_404", 404)

        from .utils import load_datas

        try:
            genre_data = load_datas(genres)

            resp = message(True, "Genres data sent")
            resp["genres"] = genre_data
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def save_genre(data):
        # Assign vars

        # Required values
        description = data["description"]

        try:
            new_genre = Genre(
                description=description
            )

            db.session.add(new_genre)
            db.session.flush()

            # Load the new movie info
            genre_info = genre_schema.dump(new_genre)

            # Commit changes to DB
            db.session.commit()

            resp = message(True, "Genre has successfully been created")
            resp["genre"] = genre_info

            return resp, 201

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def get_genre(genre_id):
        if not (genre := Genre.query.get(genre_id)):
            return err_resp("Genre not found!", "genre_404", 404)

        from .utils import load_data

        try:
            genre_info = load_data(genre)

            resp = message(True, "Genre data sent")
            resp["genre"] = genre_info
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def update_genre(genre_id, data):
        if not (genre := Genre.query.get(genre_id)):
            return err_resp("Genre not found!", "genre_404", 404)

        # Assign vars

        # Required values
        description = data["description"]

        try:
            genre.description = description

            db.session.add(genre)
            db.session.flush()

            # Load the new movie info
            genre_info = genre_schema.dump(genre)

            # Commit changes to DB
            db.session.commit()

            resp = message(True, "Genre has successfully been updated")
            resp["genre"] = genre_info

            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def delete_genre(genre_id):
        if not (genre := Genre.query.get(genre_id)):
            return err_resp("Genre not found!", "genre_404", 404)

        try:
            db.session.delete(genre)
            db.session.flush()
            db.session.commit()

            resp = message(True, "Genre has successfully been deleted")
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
