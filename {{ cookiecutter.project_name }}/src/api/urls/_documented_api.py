from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('api/', include('api.urls.documented')),
]
