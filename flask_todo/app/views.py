# -*- coding: utf-8 -*-
# @Date    : 2017-07-11 19:51:00
# @Author  : lileilei
#
from flask import request,redirect,session,url_for,render_template,flash
from app import app,db
from app.models import User,Tag,Event
from app.froms import regs,logi,new_event
import datetime,time
from flask_mail import Mail,Message
from celery import  Celery
mail=Mail(app)
celery = Celery(app.name)
@celery.task
def send_async_email(msg):
    with app.app_context():
        mail.send(msg)
@app.route('/',methods=['GET','POST'])
def index():
	if not session.get('username'):
		return redirect(url_for('login'))
	userde=session.get('username')
	user_id=User.query.filter_by(user=userde).first().id
	tag_id=Tag.query.filter_by(tag='重要紧急').first().id
	zhongyao=Event.query.filter_by(user_id=user_id,tag_id=tag_id).all()
	tags_id=Tag.query.filter_by(tag='重要不紧急').first().id
	zhongyao1=Event.query.filter_by(user_id=user_id,tag_id=tags_id).all()
	tag1_id=Tag.query.filter_by(tag='紧急不重要').first().id
	zhongyao2=Event.query.filter_by(user_id=user_id,tag_id=tag1_id).all()
	tag2_id=Tag.query.filter_by(tag='不重要不紧急').first().id
	zhongyao3=Event.query.filter_by(user_id=user_id,tag_id=tag2_id).all()
	return render_template('index.html',zhongyao=zhongyao,
		zhongyaofei=zhongyao1,buzhongyao=zhongyao2,bzhong=zhongyao3) 
@app.route('/login',methods=['GET',"POST"])
def login():
	form=logi()
	if form.validate_on_submit():
		username=form.username.data
		password=form.password.data
		try:
			me=User.query.filter_by(user=username).first()
			if me.password==password:
				session['username']=username
				return redirect(url_for('index'))
			else:
				flash('密码错误，请重新登录')
				return render_template('login.html',form=form)
		except:
			flash('用户名不存在')
			return render_template('login.html',form=form)
	return render_template('login.html',form=form)
@app.route('/reg',methods=['GET','POST'])
def reg():
	form=regs()
	if form.validate_on_submit():
		username=form.username.data
		password=form.password.data
		querenpassword=form.queren_pass.data
		email=form.email.data
		msg=Message(subject='您已经成功注册！',recipients=['15964636199@139.com'])
		msg.body = u'您已经成功注册todolist！可以登录使用您的账号'
		if password !=querenpassword:
			flash('请确认两次密码是否一致')
			return render_template('reg.html',form=form)
		else:
			user=User.query.filter_by(user=username).first()
			if user:
				flash('用户名已经存在')
				return render_template('reg.html',form=form)
			emai=User.query.filter_by(email=email).first()
			if emai:
				flash('邮箱已经注册')
				return render_template('reg.html',form=form)
			new_user=User(user=username,email=email,password=password)
			db.session.add(new_user)
			db.session.commit()
			return redirect('login')
	return render_template('reg.html',form=form)
@app.route('/new',methods=['GET','POST'])
def new():
	if not session.get('username'):
		return redirect(url_for('login'))
	userde=session.get('username')
	user_id=User.query.filter_by(user=userde).first().id
	form=new_event()
	if form.validate_on_submit:
		user=session.get('username')
		titles=form.title.data
		text=form.text.data
		tag=request.form.get('optionsRadios')
		start=request.form.get('starttime')
		end=request.form.get('endtime')
		if  titles is None or text is None or tag is None or start is None or end is None:
			flash('事项不能为空')
			return render_template('new.html',form=form)
		start= datetime.datetime.strptime(start,"%Y-%m-%d")
		end=datetime.datetime.strptime(end, "%Y-%m-%d")
		now=time.strftime('%Y-%m-%d',time.localtime(time.time()))
		now=datetime.datetime.strptime(now,"%Y-%m-%d")
		if end<=start:
			flash('结束时间不能小于开始时间')
			return render_template('new.html',form=form)
		if start <=now:
			flash('结束时间不能当前时间')
			return render_template('new.html',form=form)
		new_eve=Event(title=titles,text=text,starttime=start,endtime=end,
			tag_id=Tag.query.filter_by(tag=tag).first().id,
			user_id=user_id)
		db.session.add(new_eve)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('new.html',form=form)	
