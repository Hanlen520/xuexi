# -*- coding: utf-8 -*-
# @Date    : 2017-07-10 14:12:28
# @Author  : lileilei 
from flask import Flask,request,render_template,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
import datetime,os
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='123456'
db=SQLAlchemy(app)
class Comment(db.Model):
	__tablename__='comments'
	id=db.Column(db.Integer(),unique=True,primary_key=True)
	coment_date=db.Column(db.DateTime(),default=datetime.datetime.now())
	user=db.Column(db.String(),unique=True)
	text=db.Column(db.Text(),nullable=False)
	def __repr__(self):
		return self.user
@app.route('/beijing',methods=['GET',"POST"])
def beijing():
	user=request.form.get('user')
	text=request.form.get('text')
	if user is None or text is None:
		comment=Comment.query.all()
		return render_template('index.html',comments=comment)
	if user =='' or text =='':
		comment=Comment.query.all()
		return render_template('index.html',comments=comment)
	user=Comment(user=user)
	user.text=text
	db.session.add(user)
	db.session.commit()
	comment=Comment.query.all()
	return render_template('index.html',comments=comment)
if __name__ == '__main__':
	app.run(debug=True)