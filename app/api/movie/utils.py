def load_datas(movie_db_obj):
    """ Load movie datas

    Parameters:
    - Movies db objects
    """
    from app.models.schemas import MovieSchema

    movie_schema = MovieSchema(many=True)

    data = movie_schema.dump(movie_db_obj)

    return data
