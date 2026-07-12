import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Metek_Agency') 
application = get_wsgi_application()
