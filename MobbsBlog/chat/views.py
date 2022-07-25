from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room

@login_required
def roomsView(request):
    rooms = Room.objects.all()

    return render (request, 'index.html', {'rooms':rooms})

@login_required
def chatView(request, slug):
    room = Room.objects.get(slug=slug)

    return render (request, 'room.html', {'room':room})