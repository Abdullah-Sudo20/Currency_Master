import os
from django.core.wsgi import get_wsgi_application

# 🔥 CHANGE THIS to your real project folder name
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Currency_Master.settings")

application = get_wsgi_application()