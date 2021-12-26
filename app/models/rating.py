from sqlalchemy.orm import backref
from app import db, bcrypt


class Rating(db.Model):
    """ Rating model for storing rating related data """
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, db.Sequence('rating_seq'), primary_key=True)
    rating = db.Column(db.Float)
    user_id = db.Column(db.Integer)  # refactor fk pk
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))

    def __init__(self, **kwargs):
        super(Rating, self).__init__(**kwargs)
