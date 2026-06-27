from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from registration.views import apply_now, home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('apply/', apply_now, name='apply_now'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)