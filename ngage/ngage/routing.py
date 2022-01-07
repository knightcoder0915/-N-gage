from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat_room.routing
application=ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            chat_room.routing.websocket_urlpatterns
        )
    )
})