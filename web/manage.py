from flask.cli import FlaskGroup

from app import app, db
from app.models.contact import Contact
from app.models.blogentry import BlogEntry

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()




@cli.command("seed_db")
def seed_db():
    db.session.add(Contact(firstname='สมชาย', lastname='ทรงแบด', phone='081-111-1111',date = '55555'))
    db.session.add(BlogEntry(name='สมชาย', message ='081-111-1111', email ='th@gmail.com'))
    db.session.add(BlogEntry(name='สมชcccccาย', message ='081-111-111ccccc1', email ='cccccccccth@gmail.com'))
    db.session.add(BlogEntry(name='สมasdasdชcccccาย', message ='081-asdasd111-111ccccc1', email ='cccccadasdasccccth@gmail.com'))
    db.session.add(BlogEntry(name='สมasdasdชcccccาย', message ='081-asdasd11asfsafsa1-111ccccc1', email ='cccccadasdasccccth@gmaildasdasdsaasfasfa.com'))
    db.session.commit()




if __name__ == "__main__":
    cli()

