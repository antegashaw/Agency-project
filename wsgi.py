import os
import sys

project_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()