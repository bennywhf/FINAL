from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import datetime
from models import *
from django.shortcuts import redirect
# Create your views here.

def index(request):
    s = Event.objects.all()
    s.reverse()
    sa = Event.objects.filter(ttype = 'volvo')
    sa.reverse()
    st = Event.objects.filter(ttype = 'saab')
    st.reverse()
    sf = Event.objects.filter(ttype = 'fiat')
    sf.reverse()
    sp = Event.objects.filter(ttype = 'audi')
    sp.reverse()
    return render(request,'fort.html',{'events' : s, 'art':sa,'tech':st,'food':sf,'park':sp})

def AddUser(request):
    return HttpResponse('in progress')

def AddEvent(request):
    _type = request.POST['type']
    details = request.POST['details']
    link = request.POST['url']
    title= request.POST['title']
    e = Event(ttype = _type, time = datetime.now(), title = title, details = details, link = link, user = Use.objects.all()[0])
    e.save()
    return redirect ('/')

