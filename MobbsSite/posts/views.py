from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import PostForm
from posts.models import Post

# Create your views here.

def post_search_view(request):
    """Takes a search request and renders the corresponding post"""
    query_dict = request.GET
    try:
        query = int(query_dict.get('q'))
    except:
        query = None

    post_obj = None
    if query is not None:
        post_obj = Post.objects.get(id=query)
    context = {
        "object": post_obj
    }
    return render(request, 'posts/search.html', context=context)

@login_required
def post_create_view(request):
    """Takes in a post and creates it"""
    # print(request.POST)
    form = PostForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            print(title, content)
            post_object = Post.objects.create(title=title, content=content, likes=0)
            context['title'] = title
            context['content'] = content
            context['object'] = post_object
            context['created'] = True
    return render(request, "posts/create.html", context=context)

def post_detail_view(request, id):
    """Takes in a post and id and renders a post"""
    post_obj = None
    if id is not None:
        post_obj = Post.objects.get(id=id)
    context = {
        "object": post_obj,
        "title": post_obj.title,
        "content": post_obj.content,
        "likes": post_obj.likes
    }
    if request.method == "POST":
        Post.objects.update(id=id, title=post_obj.title, content=post_obj.content, likes=post_obj.likes+1)

    return render(request, "posts/detail.html", context=context)