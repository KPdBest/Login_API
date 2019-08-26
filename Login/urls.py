from django.contrib import admin
from django.conf.urls import url , include
from Test import views
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^data/', include('Test.urls'))

]
  

