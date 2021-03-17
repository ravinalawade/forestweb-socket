"""
ASGI config for server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

# application = get_asgi_application()

# import os

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# import main.routing

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

# application = ProtocolTypeRouter({
#   "http": get_asgi_application(),
#   "websocket": AuthMiddlewareStack(
#         URLRouter(
#             main.routing.websocket_urlpatterns
#         )
#     ),
# })

# import os

# from django.conf.urls import url
# from django.core.asgi import get_asgi_application

# import main.routing

# # Fetch Django ASGI application early to ensure AppRegistry is populated
# # before importing consumers and AuthMiddlewareStack that may import ORM
# # models.
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
# django_asgi_app = get_asgi_application()

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.layers import get_channel_layer

# channel_layer=get_channel_layer()

# application = ProtocolTypeRouter({
#     # Django's ASGI application to handle traditional HTTP requests
#     "http": django_asgi_app,

#     # WebSocket chat handler
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             main.routing.websocket_urlpatterns
#         )
#     ),
# })
import os
import django
from channels.routing import get_default_application
from channels.layers import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
django.setup()
channel_layer = get_channel_layer()
application = get_default_application()