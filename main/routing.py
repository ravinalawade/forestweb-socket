from django.urls import re_path, path
from . import views

websocket_urlpatterns = [
    # re_path(r'ws/chat/(?P<friendship_id>\w+)/$', consumers.ChatConsumer.as_asgi()),
    path('test', views.Websocket.as_asgi(), name='test'),
]