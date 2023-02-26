from flask.cli import FlaskGroup
from werkzeug.security import generate_password_hash
from app import app, db
from app.models.contact import Contact
from app.models.blogentry import BlogEntry
from app.models.authuser import AuthUser, PrivateContact, PrivateBlog
cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()




@cli.command("seed_db")
def seed_db():
    db.session.add(AuthUser(email="flask@204212", name='สมชาย ทรงแบด',password=generate_password_hash('1234',method='sha256'),avatar_url='https://ui-avatars.com/api/?name=\สมชาย+ทรงแบด&background=83ee03&color=fff'))
    db.session.add(AuthUser(email="ken@204212", name='สมชาย ทรงd,',password=generate_password_hash('1234',method='sha256'),avatar_url='https://ui-avatars.com/api/?name=\สมชาย+ทรงแบด&background=83ee03&color=fff'))
    db.session.add(AuthUser(email="pop@204212", name='สมชาย ทรงd,',password=generate_password_hash('1234',method='sha256'),avatar_url='https://ui-avatars.com/api/?name=\สมชาย+ทรงแบด&background=83ee03&color=fff'))
    db.session.add(PrivateContact(firstname='ส้มโอ', lastname='โอเค',phone='081-111-1112', owner_id=1))
    db.session.add(PrivateBlog(name='ส้มโอ', message='โอเค',email='flask@204212', owner_id=1))
    db.session.add(PrivateBlog(name='yom', message='โอเค',email='ken@204212o', owner_id=2))
    db.session.add(PrivateBlog(name='yodddm', message='โอเdddค',email='pop@204212', owner_id=3))
    db.session.commit()




if __name__ == "__main__":
    cli()

