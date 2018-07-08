# -*- coding: utf-8 -*-
# @Date    : 2017-07-11 19:51:28
# @Author  : lileilei
from  flask import  Flask
from  flask_sqlalchemy import  SQLAlchemy
import os
app=Flask(__name__)
db=SQLAlchemy(app)
app.config['SECRET_KEY'] = 'BaSeQuie'
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "dev.db")
app.config['SQLALCHEMY_MIGRATE_REPO'] = os.path.join(basedir, 'db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['CSRF_ENABLED'] = True
app.config['MAIL_SERVER']='smtp.139.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '15964636199'
app.config['MAIL_PASSWORD'] ='li930423'
app.config['MAIL_DEFAULT_SENDER'] = '15964636199@139.com'
from app import  views,models
