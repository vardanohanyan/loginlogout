from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import PostModel

# Create your views here.

# def post(request):

class AboutViews(TemplateView):
    template_name = 'post/about.html'


class PostView(ListView):
    model = PostModel
    template_name = 'post/all_posts.html'
    context_object_name = 'posts'
    paginate_by = 3


class PostDetailView(DetailView):
    model = PostModel
    context_object_name = 'artyom'


class PostCreateView(CreateView):
    model = PostModel
    fields = ['title', 'description', 'image']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return redirect('posts-home')