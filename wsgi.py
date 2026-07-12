import os
import sys
from django.core.wsgi import get_wsgi_application

# የፕሮጀክትህ ማህደር ወደ ሲስተሙ እንዲገባ እናደርገዋለን
sys.path.insert(0, os.path.dirname(file))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()