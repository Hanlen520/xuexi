# -*- coding: utf-8 -*-
# @Date    : 2017-07-10 20:39:57
# @Author  : lileilei
from bottle import route,redirect,template,run,Bottle,request,view
import sqlite3,datetime
app=Bottle()
@app.route('/',method='GET')
@view('liuyan')
def index():
    cnn=sqlite3.connect('data.sqlite')
    c = cnn.cursor()
    try:
        c.execute('SELECT * FROM comments')
        result=c.fetchall()
        c.close()
        return {'liuyans':result}
    except:
        return {'liuyans':''}
@app.route('/liuyan',method=['POST','GET'])
def liuyan():
    cnn=sqlite3.connect('data.sqlite')
    c = cnn.cursor()
    user=request.forms.get('user')
    tex=request.forms.get('text') 
    user_date=datetime.datetime.now()
    print(user,tex)
    if user is None or tex is None or tex ==''or user=='':
        pass
    c.execute("INSERT INTO comments(user,text,coment_date) VALUES(?,?,?)",(user,tex,user_date))
    cnn.commit()
    return redirect('/')
if __name__ == '__main__':
    run(app,debug=True,host='localhost',port=8078)
