from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('vote', views.voteOnOption, name='vote'),
    path('register', views.register, name='register')
]