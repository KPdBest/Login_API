from django.conf.urls import url
from .views import run

urlpatterns = [
    url(r'^$', run)
    
]