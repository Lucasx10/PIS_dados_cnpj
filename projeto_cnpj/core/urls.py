from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('cnpj.urls')),
    path('admin/', admin.site.urls),
    path('cnpj/', include('cnpj.urls'))
]
