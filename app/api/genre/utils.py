def load_data(genre_db_obj):
    """ Load genre data

    Parameters:
    - Genre db object
    """
    from app.models.schemas import GenreSchema

    genre_schema = GenreSchema()

    data = genre_schema.dump(genre_db_obj)

    return data


def load_datas(genre_db_objs):
    """ Load genre datas

    Parameters:
    - Genres db object
    """
    from app.models.schemas import GenreSchema

    genre_schema = GenreSchema(many=True)

    data = genre_schema.dump(genre_db_objs)

    return data
