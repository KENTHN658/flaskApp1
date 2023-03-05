from flask_login import UserMixin
from app import db

from sqlalchemy_serializer import SerializerMixin
from .contact import Contact
from .blogentry import BlogEntry
from .moods import Moody

class AuthUser(db.Model, UserMixin, SerializerMixin):
    __tablename__ = "auth_users"
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(1000))
    password = db.Column(db.String(100))
    avatar_url = db.Column(db.String(100))


    def __init__(self, email, name, password, avatar_url):
        self.email = email
        self.name = name
        self.password = password
        self.avatar_url = avatar_url

    def update(self, email, name, password, avatar_url):
        self.email = email
        self.name = name
        self.password = password
        self.avatar_url = avatar_url

class PrivateContact(Contact, UserMixin, SerializerMixin):
    owner_id = db.Column(db.Integer, db.ForeignKey('auth_users.id'))


    def __init__(self, firstname, lastname, phone, owner_id):
        super().__init__(firstname, lastname, phone)
        self.owner_id = owner_id


class PrivateBlog(BlogEntry, UserMixin, SerializerMixin):
    owner_id = db.Column(db.Integer, db.ForeignKey('auth_users.id'))

    def __init__(self, name, message, email, owner_id):
        super().__init__( name, message, email)
        self.owner_id = owner_id

    def update(self, name, message, email, owner_id):
        super().__init__( name, message, email)
        self.owner_id = owner_id


class PrivateMood(Moody, UserMixin, SerializerMixin):
    owner_id = db.Column(db.Integer, db.ForeignKey('auth_users.id'))

    def __init__(self, sleep, meditation, mind, boring, social, messages, pivate, owner_id):
        super().__init__( sleep, meditation, mind, boring, social, messages, pivate)
        self.owner_id = owner_id

    def update(self, sleep, meditation, mind, boring, social, messages, pivate, owner_id):
        super().__init__( sleep, meditation, mind, boring, social, messages, pivate)
        self.owner_id = owner_id

    

