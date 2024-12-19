import os
from django.core.wsgi import get_wsgi_application
from pathlib import Path
path=Path("C:\api\.venv\testapi\settings.py")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testapi.settings')
application = get_wsgi_application()