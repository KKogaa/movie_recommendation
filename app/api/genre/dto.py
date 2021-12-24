from flask_restx import Namespace, fields


class GenreDto:

    api = Namespace("genres", description="Genre related operations.")
    genre = api.model(
        "Genre object",
        {
            "description": fields.String,
        },
    )

    data_resp = api.model(
        "Genre Data Response",
        {
            "description": fields.String,
        },
    )
