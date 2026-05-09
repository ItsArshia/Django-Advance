from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm

class IndexView(TemplateView):
    """
    Pascal Case name for class
    Classe Based View for blog index page
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'arshia falahi'
        return context

class RedirectToMaktab(RedirectView):
    url = "https://maktabkhooneh.org"


class PostListView(LoginRequiredMixin, ListView):
    model = Post

    context_object_name = "posts"




class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

"""
class PostCreateView(FormView):
    template_name = 'contact.html' # we have to set a template name
    form_class = PostForm
    success_url = '/blog/post'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'status', 'category', 'published_at']
    success_url = '/blog/post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/post'