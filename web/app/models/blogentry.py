from app import db
from sqlalchemy_serializer import SerializerMixin
import datetime
class BlogEntry(db.Model, SerializerMixin):
    __tablename__ = "blogentry"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    message = db.Column(db.String(280))
    email = db.Column(db.String(50))
    date_created = db.Column(db.DateTime)
    date_update = db.Column(db.DateTime)
    
    def __init__(self, name, message, email):
        self.name = name
        self.message =  message 
        self.email = email
        self.date_created = datetime.datetime.now()
        self.date_update = datetime.datetime.now()


    def update(self, name, message, email):
        self.name = name
        self.message =  message
        self.email = email
        self.date_update = datetime.datetime.now()
       