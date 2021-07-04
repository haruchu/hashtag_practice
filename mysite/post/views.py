from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Post, Tag


class ListClass(ListView):
    template_name = 'list.html'
    model = Post
    def get_queryset(self):
        tag = self.request.GET.get('tag')

        if tag:
            post_list = Post.objects.filter(
                tag__name__icontains=tag)
        else:
            post_list = Post.objects.all()
        return post_list


class FormClass(CreateView):
    template_name = 'form.html'
    model = Post
    fields = ('title', 'text')
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        post = Post(
            title=form.cleaned_data["title"], text=form.cleaned_data["text"])
        post.save()
        words = form.cleaned_data["text"].split()
        for word in words:
            if word[0] == "#":
                if Tag.objects.filter(name=word[1:]).exists():
                    tag = Tag.objects.get(name=word[1:])
                else:
                    tag = Tag.objects.create(name=word[1:])
                post.tag.add(tag)
        return redirect('list')
