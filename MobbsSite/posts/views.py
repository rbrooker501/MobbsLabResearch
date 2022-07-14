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
    context = {}
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post_obj = Post.objects.create(title=title, content=content, likes=0)
        context['object'] = post_obj
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
        post_obj.likes += 1
        post_obj.save()
        context = {
            'object': post_obj
        }
        return render(request, 'posts/search.html', context=context)

    return render(request, "posts/detail.html", context=context)