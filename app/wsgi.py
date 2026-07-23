import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings') # loyihangiz nomi 'app' bo'lsa

application = get_wsgi_application()
app = application  # <- Ushbu qator bo'lishi shart