# -*- coding: utf-8 -*-
# @Date    : 2017-07-11 10:59:21
# @Author  : lileilei 
import tornado.ioloop
import tornado.web
import sqlite3,datetime
class MainHandler(tornado.web.RequestHandler):
	def get(self,*arg,**kwargs):
		cnn=sqlite3.connect('data.sqlite')
		c = cnn.cursor()
		c.execute('SELECT * FROM comments')
		result=c.fetchall()
		c.close()
		self.render('index.html',comments=result)
	def post(self,*arg,**kwargs):
		user = self.get_argument('user')
		pwd = self.get_argument('text')
		coment_date=datetime.datetime.now()
		cnn=sqlite3.connect('data.sqlite')
		c = cnn.cursor()
		try:
			c.execute("INSERT INTO comments(user,text,coment_date) VALUES(?,?,?)",(user,pwd,coment_date))
			cnn.commit()
			c.execute('SELECT * FROM comments')
			result=c.fetchall()
			c.close()
			self.render('index.html',comments=result)
		except:
			c.execute('SELECT * FROM comments')
			result=c.fetchall()
			c.close()
			self.render('index.html',comments=result)	
settings={
	'template_path':'views',
}
application=tornado.web.Application([
	(r'/index',MainHandler)],**settings)
if __name__ == '__main__':
	application.listen(999)
	tornado.ioloop.IOLoop.instance().start()