from django.contrib import admin
from django.shortcuts import render
from django.contrib import messages
from django.db.models import Func
from django.db.models.functions import Coalesce
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Song 
import json
from django.core import serializers
from django.shortcuts import render
import json as simplejson
from django.db.models import IntegerField
from .models import Artist
from .models import Rating
from django.forms import ModelChoiceField
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db.models import Avg
import json
def index(request):
	songs=Song.objects.annotate(avg_review=Coalesce(Avg('rating__rating'),0)).order_by('-avg_review')[:10]
	artists=Artist.objects.annotate(avg_review=Coalesce(Avg('song__rating__rating'),0)).order_by('-avg_review')[:10]
	ratings=Rating.objects.all()
	alldata = { "details1" : songs, "details2" : artists,"details3":ratings}
	return render(request,'index.html',alldata)

def login(request):
	if request.user.is_authenticated:
		return redirect('/')
	if request.method =='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(request, username=username,password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request,'Invalid Credentials')
			return render(request,'login.html')
	else:
		return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
	if request.method =='POST':
		fname=request.POST['fname']
		lname=request.POST['lname']
		username=request.POST['uname']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']

		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username Taken')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email Taken')
				return redirect('register')
			else:
				user=User.objects.create_user(username=username,password=password1,email=email,first_name=fname,last_name=lname)
				user.save()
				return render(request,'login.html')
		else:
			return redirect('register')
	else:
		return render(request,'register.html')

def addsong(request):
	if request.user.is_authenticated:
		if request.method =='POST':
			user = request.user.id
			name=request.POST["name"]
			release_date=request.POST["release_date"]
			image=request.FILES["image"]
			a_id=request.POST.getlist('a_id')
			song_info=Song.objects.create(name=name,release_date=release_date,image=image,user_id=user)
			song_info.a_id.set(a_id)
			song_info.save()
			artists=Artist.objects.all()
			messages.info(request,'Song is added suuccessfully')
			return render(request,'addsong.html',{'artists':artists})
		else:
			artists=Artist.objects.all()
			return render(request,'addsong.html',{'artists':artists})
	else:
		return redirect('/login')
def artist(request):
	if request.user.is_authenticated:
		if request.is_ajax():
			name=request.POST["name"]
			dob=request.POST["dob"]
			bio=request.POST["bio"]
			artist_info=Artist.objects.create(name=name,dob=dob,bio=bio)
			artist_info.save()
			message="Artist Created"
			artists=Artist.objects.all()
			artist = Artist.objects.all()
			data = list(artist.values('id', 'name'))
			return HttpResponse(simplejson.dumps(data), content_type="application/json")
		else:
			message="Artist Not Created"
			return HttpResponse(message)
	else:
		return redirect('/addsong')
def rating(request):
	if request.user.is_authenticated:
		if request.is_ajax():
			rating=request.POST.get("rating", False)
			song=request.POST.get("song_id", False)
			user= request.user.id
			rating_info=Rating.objects.create(rating=rating,song_id=song,user_id=user)
			rating_info.save()
			message="You Give " + rating + " Star"
			return HttpResponse(message)
		else:
			message="You are already rated for this song"
			return HttpResponse(message)
	else:
		message="Login to rate"
		return HttpResponse(message)