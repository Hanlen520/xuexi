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
from app import  views,models
