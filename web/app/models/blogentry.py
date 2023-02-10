from app import db
from sqlalchemy_serializer import SerializerMixin

class BlogEntry(db.Model, SerializerMixin):
    __tablename__ = "BlogEntrys"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Colum(db.String(50))
    message = db.Column(db.String(280))
    email = db.Column(db.String(50))
    date_created = db.Column(db.String(20))
    date_update = db.Column(db.String(20))

    def __init__(self, name, message, email, date_create, date_update):
        self.name = name
        self. message =  message
        self.email = email
        self.phdate_createone = date_create
        self.date_update = date_update


    def update(self, name, message, email, date_create, date_update):
        self.name = name
        self. message =  message
        self.email = email
        self.phdate_createone = date_create
        self.date_update = date_update