"""
Renders HTML web pages
"""

from django.http import HttpResponse
from django.template.loader import render_to_string
from posts.models import Post


def home(request, *args, **kwargs):
    """Takes in a request and returnz HTML as a response"""
    post_qs = Post.objects.all()

    context = {
        "objectlist": post_qs,
    }
    HTML_STRING = render_to_string("home.html",
    context = context)
    return HttpResponse(HTML_STRING)