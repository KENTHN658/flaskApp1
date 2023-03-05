from app import db
from sqlalchemy_serializer import SerializerMixin
import datetime

class Moody(db.Model, SerializerMixin):
    __tablename__ = "mood"
    
    id = db.Column(db.Integer, primary_key=True)
    messages = db.Column(db.String(250))
    sleep = db.Column(db.String(50))
    meditation = db.Column(db.String(50))
    mind = db.Column(db.String(20))
    boring = db.Column(db.String(20))
    social = db.Column(db.String(20))
    pivate = db.Column(db.String(20))
    date_created = db.Column(db.DateTime)
    date_update = db.Column(db.DateTime)
    
    def __init__(self, sleep, meditation, mind, boring, social, messages, pivate):
        self.messages = messages
        self.sleep = sleep
        self.meditation =  meditation 
        self.mind = mind
        self.boring = boring
        self.social =  social 
        self.pivate = pivate
        self.date_created = datetime.datetime.now()
        self.date_update = datetime.datetime.now()

    def update(self, sleep, meditation, mind, boring, social, messages, pivate):
        self.messages = messages
        self.sleep = sleep
        self.meditation =  meditation 
        self.mind = mind
        self.boring = boring
        self.social =  social 
        self.pivate = pivate
        self.date_update = datetime.datetime.now()
    