from app import db
from sqlalchemy_serializer import SerializerMixin

class Contact(db.Model, SerializerMixin):
    __tablename__ = "contacts"


    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    date = db.Column(db.String(100))

    def __init__(self, firstname, lastname, phone,date):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.date = date


    def update(self, firstname, lastname, phone, date):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.date = date