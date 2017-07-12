# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 10:09:28
# @Author  : lileilei 
from flask_wtf import Form
from wtforms import PasswordField,StringField,TextAreaField,IntegerField,SubmitField,validators,DateTimeField,BooleanField,SelectMultipleField,FileField
from wtforms.validators import DataRequired
class logi(Form):
	username=StringField('用户名',[validators.length(min=6, max=16,message='用户名长度6-16'),validators.DataRequired()],render_kw={'placeholder':u'输入用户名'})
	password=PasswordField('密码',[validators.length(min=6, max=16,message='密码长度是6-16'),validators.DataRequired()],render_kw={'placeholder':u'输入密码'})
class regs(Form):
	username=StringField('用户名',[validators.length(min=6, max=16,message='用户名长度6-16'),validators.DataRequired()],render_kw={'placeholder':u'输入用户名'})
	password=PasswordField('密码',[validators.length(min=6, max=16,message='密码长度是6-16'),validators.DataRequired()],render_kw={'placeholder':u'输入密码'})
	queren_pass=PasswordField('确认密码',[validators.length(min=6, max=16,message='密码长度是6-16'),validators.DataRequired()],render_kw={'placeholder':u'输入密码'})
	email=StringField('邮箱',[validators.length(min=4,max=20,message='邮箱错误'),validators.DataRequired()])
class new_event(Form):
	title=StringField('标题',[validators.length(min=2, max=16,message='标题长度2-16'),validators.DataRequired()],render_kw={'placeholder':u'输入标题'})
	text=TextAreaField('事件内容',[validators.DataRequired()])