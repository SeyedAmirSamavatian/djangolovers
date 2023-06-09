from django.contrib import admin
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static
from .views import welcome , base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome , name='welcome'),
    path('accounts/', include('accounts.urls')), 
    path('home/', include('contents.urls')), 
    path('otheruser/', include('otheruser.urls')), 
    path('chat/', include('chat.urls')), 
    path('onlines/', include('onlines.urls')), 
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)