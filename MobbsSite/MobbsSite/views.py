"""
Renders HTML web pages
"""

from django.http import HttpResponse


def home(request):
    """Take in a request and return HTML as a response"""
    name = 'Riley'
    HTML_STRING = f"""
    <h1>Hello {name}!</h1>
    """
    return HttpResponse(HTML_STRING)