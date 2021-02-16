"""users/urls.py"""
# django modules
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import url
from django.urls import path

# My modules
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='users/login.html'), name='logout'),
    url(r'^register/$', views.register, name='register'),

]
