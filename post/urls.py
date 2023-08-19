from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.PostList.as_view(),name='post_list'),
    path('<int:pk>/', views.PostDetaile.as_view(),name='post_detailes')
]