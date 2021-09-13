from datetime import date

from app.models import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    phone = db.Column(db.Integer, unique=True)
    address = db.Column(db.Text)
    created_date = db.Column(db.Date, default=date.today())
    updated_date = db.Column(db.Date, onupdate=date.today())

    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def __repr__(self):
        return "<User %r>" % self.id