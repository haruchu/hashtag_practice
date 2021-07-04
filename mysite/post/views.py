from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Post


class ListClass(ListView):
    template_name = 'list.html'
    model = Post


class FormClass(CreateView):
    template_name = 'form.html'
    model = Post
    fields = ('title', 'text')
    success_url = reverse_lazy('list')

