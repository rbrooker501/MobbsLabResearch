"""
Loads the relevant views for the page that the user is on.
"""

from django.shortcuts import render

def indexView(request):
    """Loads index.html upon request"""
    return render(request, 'chat/index.html')

def roomView(request, room_name):
    """Loads the chat room that the user is in"""
    return render(request, 'chat/room.html', {
        'room_name': room_name,
    })