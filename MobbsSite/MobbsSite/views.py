"""
Renders HTML web pages
"""

from django.http import HttpResponse
from django.template.loader import render_to_string
from posts.models import Post


def home(request):
    """Take in a request and return HTML as a response"""
    post_obj = Post.objects.get(id=1)
    post_qs = Post.objects.all()

    context = {
        "objectlist": post_qs,
        "title": post_obj.title,
        "content": post_obj.content,
        "likes": post_obj.likes
    }
    H_STRING = render_to_string("home.html",
    context = context)

    HTML_STRING = H_STRING
    return HttpResponse(HTML_STRING)