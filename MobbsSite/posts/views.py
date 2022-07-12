from django.shortcuts import render

from posts.models import Post

# Create your views here.
def post_detail_view(request, id):
    post_obj = Post.objects.get(id=1)
    context = {
        "object": post_obj,
        "title": post_obj.title,
        "content": post_obj.content,
        "likes": post_obj.likes
    }

    return render(request, "posts/detail.html", context = context)