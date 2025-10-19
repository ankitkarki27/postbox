from django.urls import path
from .consumers import ChatroomConsumer

websocket_urlpatterns = [
    # DYNAMIC PARAMETERS IN URLS
    path('ws/chatroom/<chatroom_name>/', ChatroomConsumer.as_asgi()),
]