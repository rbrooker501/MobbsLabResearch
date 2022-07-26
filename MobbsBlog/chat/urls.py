# chat/urls.py
from django.urls import path

from .views import indexView, roomView

urlpatterns = [
    path('', indexView, name='chat'),
    path('<str:room_name>/', roomView, name='room'),
]