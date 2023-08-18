from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'post'
urlpatterns = [
    path('/post_list', views.post_list,name='post_list'),
    path('/post_detailes', views.post_detailes,name='post_detailes')
]