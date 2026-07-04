import os
import sys

# የፕሮጀክቱ ፋይል ያለበትን ቦታ ለDjango እንንገረው
sys.path.insert(0, os.path.abspath(os.path.dirname(file)))

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
application = get_wsgi_application()