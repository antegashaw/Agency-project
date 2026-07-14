from django.core.wsgi import get_wsgi_application

# የፎልደሩ ስም ADDIS_AGENCY ስለሆነ settings የሚለው በውስጡ ነው ያለው
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ADDIS_AGENCY.settings')

application = get_wsgi_application()