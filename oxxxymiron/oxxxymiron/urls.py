from django.contrib import admin
from django.urls import path, include
from oxxxymiron import settings
from django.conf.urls.static import static
from oxxxy2.views import main


urlpatterns = [
    path('admin/', admin.site.urls),
    path('oxxxy2/', include('oxxxy2.urls')),
    path('', main, name='main')
]
