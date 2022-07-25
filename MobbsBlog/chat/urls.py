from django.urls import path

from .views import roomsView, chatView

urlpatterns = [
    path('', roomsView, name='room-select'),
    path('<slug:slug>/', chatView, name='chat-room')
]