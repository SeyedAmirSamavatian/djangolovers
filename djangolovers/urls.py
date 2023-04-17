from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import welcome , base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome , name='welcome'),
    path('base/', base , name='base'),  #movaghati
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)