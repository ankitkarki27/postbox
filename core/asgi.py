import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# initilizes the ASGI application
django_asgi_app = get_asgi_application()

# after initializing the django application we can import the routing module
from chat import routing

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        # Just HTTP for now. (We can add other protocols later.)
        # web sockets protocol now:
        
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    routing.websocket_urlpatterns
                )
            )
        )
    }
)

