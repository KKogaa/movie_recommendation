from app import db, bcrypt


class Genre(db.Model):
    """ Genre model for storing genre related data """
    __tablename__ = 'genres'

    id = db.Column(db.Integer, db.Sequence('genre_seq'), primary_key=True)
    description = db.Column(db.String(64), unique=True, index=True)

    def __init__(self, **kwargs):
        super(Genre, self).__init__(**kwargs)

    # def __repr__(self):
    #     return f"<User {self.username}>"
