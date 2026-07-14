import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# ይህ 'application' የሚለው ቃል ነው Vercel የሚፈልገው!
application = get_wsgi_application()