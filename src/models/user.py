from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    pword = db.Column(db.String(150))
    time_created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())

    def __init__(self, username, pword):
        self.username = username
        self.pword = pword

    def __repr__(self) -> str:
        return f"User with username={self.username}, time_created={self.time_created})>"