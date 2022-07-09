"""
Loads the relevant views for the page that the user is on.
"""

from django.shortcuts import render

def index(request):
    """Loads index.html upon request"""
    return render(request, 'chat/index.html')

def login(request):
    """Loads login.html"""
    return render(request, 'chat/login.html')

def room(request, room_name):
    """Loads the chat room that the user is in"""
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })