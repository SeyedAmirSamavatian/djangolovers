from django.urls import path
from .views import showOnline

urlpatterns = [
    path('', showOnline  , name='showOnline'),
]