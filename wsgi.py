import os
import sys

# የፕሮጀክትህን ዋና ፎልደር ወደ ሲስተም መንገድ ጨምር
sys.path.append(os.getcwd())

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()