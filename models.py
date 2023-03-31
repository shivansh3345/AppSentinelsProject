from flask_login import UserMixin
from config import db

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=True, nullable=False)
    def __repr__(self):
        return f"User '{self.user_id}','{self.email}'"

    def get_id(self):
        return (self.user_id)
