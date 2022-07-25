from django.urls import path

from .views import roomsView

urlpatterns = [
    path('', roomsView, name='room-select')
]