"""
Loads the relevant views for the page that the user is on.
"""

from ast import Del
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.http import HttpResponseRedirect

def LikeView(request, pk):
    """Handles likes on a post.
    Arguments:
      `pk`: The id of the post to like
    """
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


class HomeView(ListView):
    """Creates the view for the homepage.
    Orders all posts in order from most to least recent
    """
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date', '-id']

class PostDetailView(DetailView):
    """Creates the view to view posts."""
    model = Post
    template_name = 'post_detail.html'
    def get_context_data(self, *args, **kwargs):
        # Shows and makes the like button functional
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post.total_likes()
        liked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class PostCreateView(CreateView):
    """Creates the view to make a post"""
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'

class PostEditView(UpdateView):
    """Creates the view to edit a post"""
    model = Post
    form_class = EditForm
    template_name = 'post_edit.html'

class PostDeleteView(DeleteView):
    """Creates the view to delete a post"""
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class MyPostsView(ListView):
    """Creates a view to list all posts by the user"""
    model = Post
    template_name = 'my_posts.html'
    ordering = ['-post_date', '-id']

class AddCommentView(CreateView):
    """Creates a view to add a comment to a post"""
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})
