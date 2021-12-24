from flask_restx import Namespace, fields


class MovieDto:

    api = Namespace("movies", description="Movie related operations.")
    movie = api.model(
        "Movie object",
        {
            "title": fields.String,
        },
    )

    data_resp = api.model(
        "User Data Response",
        {
            "title": fields.String,
        },
    )
