from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import Post

# Create your views here.
class PostList(ListView):
    model = Post

class PostDetaile(DetailView):
    model = Post