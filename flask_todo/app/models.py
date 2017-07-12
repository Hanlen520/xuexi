# -*- coding: utf-8 -*-
# @Date    : 2017-07-11 19:52:52
# @Author  : lileilei
from app import app,db
import datetime
from werkzeug.security import check_password_hash,generate_password_hash
class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer(),primary_key=True,autoincrement=True)
    user=db.Column(db.String(252),unique=True)
    password=db.Column(db.String(252))
    email=db.Column(db.String(252),unique=True)
    def __repr__(self):
        return  self.user
class Event(db.Model):
    __tablename__='events'
    id=db.Column(db.Integer(),primary_key=True,autoincrement=True)
    title=db.Column(db.String(),autoincrement=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    text=db.Column(db.Text())
    starttime=db.Column(db.DateTime(),default=datetime.datetime.now())
    endtime=db.Column(db.DateTime())
    tag_id=db.Column(db.Integer(),db.ForeignKey('tags.id'))
    def __repr__(self):
        return self.title
class Tag(db.Model):
    __tablename__='tags'
    id=db.Column(db.Integer(),primary_key=True)
    tag=db.Column(db.String(64))
    def __repr__(self):
        return  self.tag
