from django.urls import path, include
from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('vote', views.voteOnOption, name='vote'),
    path('register/', views.register, name='register'),
    path('logout', views.logout_view, name="logout"),
]