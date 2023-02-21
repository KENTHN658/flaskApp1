from flask import (jsonify, render_template,
                   request, url_for, flash, redirect)
import json
from sqlalchemy.sql import text
from app import app
from app import db
from app.models.contact import Contact
from app.models.blogentry import BlogEntry
import datetime



@app.route('/')
def home():
    return "Flask says 'Hello world!'"


@app.route('/crash')
def crash():
    return 1/0

@app.route('/db')
def db_connection():
    try:
        with db.engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return '<h1>db works.</h1>'
    except Exception as e:
        return '<h1>db is broken.</h1>' + str(e)

@app.route('/lab11', methods=('GET', 'POST'))
def lab11_bootstrap():
    if request.method == 'POST':
        result = request.form.to_dict()
        app.logger.debug(str(result))
        id_ = result.get('id', '')
        validated = True
        validated_dict = dict()
        valid_keys = ['name', 'message', 'email']


        # validate the input

        for key in result:
            # screen of unrelated inputs
            if key not in valid_keys:
                continue


            value = result[key].strip()
            if not value or value == 'undefined':
                validated = False
                break
            validated_dict[key] = value
        if validated:
            # utc_dt = datetime.datetime.now()
            # utc_dt_1 = utc_dt.strftime("%c")
            # validated_dict['date'] = utc_dt_1
            
            app.logger.debug('validated dict: ' + str(validated_dict))
            # if there is no id: create a new contact entry
            if not id_:
                entry = BlogEntry(**validated_dict)
                app.logger.debug(str(entry))
                db.session.add(entry)
            # if there is an id already: update the contact entry
            else:
                blogentry = BlogEntry.query.get(id_)
                blogentry.update(**validated_dict)


            db.session.commit()


        return lab11_db_blog()  
    return app.send_static_file('lab11_microblog.html')



@app.route('/lab04', methods=('GET', 'POST'))
def lab04_bootstrap():
    if request.method == 'POST':
        result = request.form.to_dict()
        app.logger.debug(str(result))
        id_ = result.get('id', '')
        validated = True
        validated_dict = dict()
        valid_keys = ['name', 'message', 'email']


        # validate the input

        for key in result:
            app.logger.debug(key, result[key])
            # screen of unrelated inputs
            if key not in valid_keys:
                continue


            value = result[key].strip()
            if not value or value == 'undefined':
                validated = False
                break
            validated_dict[key] = value

        
        if validated:
            # utc_dt = datetime.datetime.now()
            # utc_dt_1 = utc_dt.strftime("%c")
            # validated_dict['date'] = utc_dt_1
            
            app.logger.debug('validated dict: ' + str(validated_dict))
            # if there is no id: create a new contact entry
            if not id_:
                entry = BlogEntry(**validated_dict)
                app.logger.debug(str(entry))
                db.session.add(entry)
            # if there is an id already: update the contact entry
            else:
                blogentry = BlogEntry.query.get(id_)
                blogentry.update(**validated_dict)


            db.session.commit()


        return lab04_db_blog()  
    return app.send_static_file('lab04_bootstrap.html')


@app.route('/lab10', methods=('GET', 'POST'))
def lab10_phonebook():
    if request.method == 'POST':
        result = request.form.to_dict()
        app.logger.debug(str(result))
        id_ = result.get('id', '')
        validated = True
        validated_dict = dict()
        valid_keys = ['firstname', 'lastname', 'phone', 'date']


        # validate the input

        for key in result:
            app.logger.debug(key, result[key])
            # screen of unrelated inputs
            if key not in valid_keys:
                continue


            value = result[key].strip()
            if not value or value == 'undefined':
                validated = False
                break
            validated_dict[key] = value

        
        if validated:
            utc_dt = datetime.datetime.now()
            utc_dt_1 = utc_dt.strftime("%c")
            validated_dict['date'] = utc_dt_1
            
            app.logger.debug('validated dict: ' + str(validated_dict))
            # if there is no id: create a new contact entry
            if not id_:
                entry = Contact(**validated_dict)
                app.logger.debug(str(entry))
                db.session.add(entry)
            # if there is an id already: update the contact entry
            else:
                contact = Contact.query.get(id_)
                contact.update(**validated_dict)


            db.session.commit()


        return lab10_db_contacts()
    return app.send_static_file('lab10_phonebook.html')


@app.route("/lab10/contacts")
def lab10_db_contacts():
    contacts = []
    db_contacts = Contact.query.all()


    contacts = list(map(lambda x: x.to_dict(), db_contacts))
    app.logger.debug("DB Contacts: " + str(contacts))


    return jsonify(contacts)

@app.route("/lab04/blog")
def lab04_db_blog():
    blogEntrys = []
    # https://stackoverflow.com/questions/15791760/how-can-i-do-multiple-order-by-in-flask-sqlalchemy
    db_blogentry = BlogEntry.query.order_by(BlogEntry.date_update.desc()).all()
    
    blogEntrys = list(map(lambda x: x.to_dict(), db_blogentry))
    app.logger.debug("DB blog: " + str(blogEntrys))
    
    return jsonify(blogEntrys)

@app.route("/lab11/blog")
def lab11_db_blog():
    blogEntrys = []
    # https://stackoverflow.com/questions/15791760/how-can-i-do-multiple-order-by-in-flask-sqlalchemy
    db_blogentry = BlogEntry.query.order_by(BlogEntry.date_update.desc()).all()
    
    blogEntrys = list(map(lambda x: x.to_dict(), db_blogentry))
    app.logger.debug("DB blog: " + str(blogEntrys))
    
    return jsonify(blogEntrys)

@app.route('/lab10/remove_contact', methods=('GET', 'POST'))
def lab10_remove_contacts():
    app.logger.debug("LAB10 - REMOVE")
    if request.method == 'POST':
        result = request.form.to_dict()
        id_ = result.get('id', '')
        try:
            contact = Contact.query.get(id_)
            db.session.delete(contact)
            db.session.commit()
        except Exception as ex:
            app.logger.debug(ex)
            raise
    return lab10_db_contacts()

@app.route('/lab04/remove_blog', methods=('GET', 'POST'))
def lab04_remove_blog():
    app.logger.debug("LAB04 - REMOVE")
    if request.method == 'POST':
        result = request.form.to_dict()
        id_ = result.get('id', '')
        try:
            blog = BlogEntry.query.get(id_)
            db.session.delete(blog)
            db.session.commit()
        except Exception as ex:
            app.logger.debug(ex)
            raise
    return lab04_db_blog()

@app.route('/lab11/remove_blog', methods=('GET', 'POST'))
def lab11_remove_blog():
    app.logger.debug("LAB11 - REMOVE")
    if request.method == 'POST':
        result = request.form.to_dict()
        id_ = result.get('id', '')
        try:
            blog = BlogEntry.query.get(id_)
            db.session.delete(blog)
            db.session.commit()
        except Exception as ex:
            app.logger.debug(ex)
            raise
    return lab11_db_blog()