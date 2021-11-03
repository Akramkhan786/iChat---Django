from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('iChat/', consumers.ChatConsumer.as_asgi()),
]