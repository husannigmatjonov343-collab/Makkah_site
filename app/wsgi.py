import os
from django.core.wsgi import get_wsgi_application

# Bu yerda loyiha papkasi 'app' ekani ko'rsatilgan bo'lishi shart:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()

# Vercel talab qiladigan o'zgaruvchi:
app = application

import os
import sys

# Python ildiz katalogidagi modullarni topishi uchun yo'lni ko'rsatamiz
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


application = get_wsgi_application()
