from django.contrib import admin
from django.urls import path
from registration.views import apply_now, home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),          # ዌብሳይቱ ሲከፈት መጀመሪያ ዋናውን ገጽ ያሳያል
    path('apply/', apply_now, name='apply_now'), # /apply/ ሲባል ደግሞ ፎርሙን ያሳያል
]