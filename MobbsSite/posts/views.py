from django.shortcuts import render

from posts.models import Post

# Create your views here.

def post_search_view(request):
    query_dict = request.GET
    # query = query_dict.get('q')

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

    return render(request, "posts/detail.html", context = context)