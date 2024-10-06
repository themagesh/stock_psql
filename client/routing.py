from django.urls import re_path
from client import consumers  # Import consumers

websocket_urlpatterns = [
    re_path(r'ws/ticker/$', consumers.TickerConsumer.as_asgi()),  # WebSocket route
]
