from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from registration.views import apply_now, home_page
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),      # ይህንን መስመር ጨምር
    path('apply/', views.apply, name='apply'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('apply/', apply_now, name='apply_now'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)