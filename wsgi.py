import os
import sys

# የፕሮጀክትህ Root ፎልደር ወደ Path እንዲገባ እናድርግ
sys.path.insert(0, os.path.dirname(os.path.abspath(file)))

# የ settings ፋይል ያለበትን መንገድ በግልጽ እንንገረው
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()