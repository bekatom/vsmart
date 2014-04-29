# -*- coding: utf-8 -*-
import datetime
from flask import url_for
from flaskstarter import db
from mongoengine import *


class User(db.Document):
    user_name = db.StringField(max_length=100)
    password = db.StringField(max_length=100)
    email = db.StringField(max_length=100)
    create_date = db.DateTimeField(default=datetime.datetime.now)
    
class Project(db.Document):
    name = db.StringField(max_length=100)
    create_date = db.DateTimeField(default=datetime.datetime.now)
    user = db.ListField(db.ReferenceField(User))

class Task(db.Document):
    title = db.StringField(max_length=300)
    description = db.StringField(max_length=1024)
    create_date = db.DateTimeField(default=datetime.datetime.now)
    assign_to = db.ListField(db.ReferenceField(User))
    project = db.ReferenceField(Project)
    due_date = db.DateTimeField()
