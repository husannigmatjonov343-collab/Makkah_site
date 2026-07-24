import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings') # loyihangiz nomi 'app' bo'lsa

application = get_wsgi_application()
app = application  # <- Ushbu qator bo'lishi shart

import os
import sys

# Python ildiz katalogidagi modullarni topishi uchun yo'lni ko'rsatamiz
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()
