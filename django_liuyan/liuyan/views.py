from django.shortcuts import render,redirect
from  django.http import  HttpResponse,HttpResponseRedirect
from .models import Comment
import datetime
# Create your views here.
def hello(request):
    comments=Comment.objects.all()
    if request.method=="POST":
        user=request.POST['user']
        text=request.POST['text']
        date=datetime.datetime.now()
        new_comment=Comment()
        new_comment.text=text
        new_comment.name=user
        new_comment.date_time=date
        new_comment.save()
        return  HttpResponseRedirect('/')
    return  render(request,'index.html',{'comments':reversed(comments)})
