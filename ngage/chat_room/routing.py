from django.conf.urls import url
from django.urls import re_path
from django.urls.conf import path

from chat_room import Consumer

websocket_urlpatterns=[
    re_path(r'ws/chat/(?P<room_name>\w+)/(?P<person_name>\w+)/$',Consumer.Consumer)
]