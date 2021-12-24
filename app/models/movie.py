from sqlalchemy.orm import backref
from app import db, bcrypt

map_table = db.Table('genre_movie', db.metadata, db.Column('genre_id', db.Integer, db.ForeignKey(
    'genres.id')), db.Column('movie_id', db.Integer, db.ForeignKey('movies.id')))


class Movie(db.Model):
    """ Movie model for storing movie related data """
    __tablename__ = 'movies'

    id = db.Column(db.Integer, db.Sequence('movie_seq'), primary_key=True)
    title = db.Column(db.String(64))

    genres = db.relationship('Genre', secondary=map_table, backref='movies')

    def __init__(self, **kwargs):
        super(Movie, self).__init__(**kwargs)

    # def __repr__(self):
    #     return f"<User {self.username}>"
