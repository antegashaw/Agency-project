import os
from django.core.wsgi import get_wsgi_application

# በ settings.py ውስጥ ያለው ስም በትክክል 'settings' መሆኑን አረጋግጥ
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()