from ast import Del
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.http import HttpResponseRedirect

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date', '-id']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        total_likes = (get_object_or_404(Post, id=self.kwargs['pk'])).total_likes()
        context['total_likes'] = total_likes
        return context

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'

class PostEditView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'post_edit.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
