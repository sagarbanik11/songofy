from django.urls import path

from . import views

urlpatterns=[
	path('',views.index,name='index'),
	path('register/',views.register,name='register'),
	path('login/',views.login,name='login'),
	path('addsong/',views.addsong,name='addsong'),
	path('artist/',views.artist,name='artist'),
	path('logout/',views.logout,name='logout'),
	path('rating/',views.rating,name='rating'),
	




]