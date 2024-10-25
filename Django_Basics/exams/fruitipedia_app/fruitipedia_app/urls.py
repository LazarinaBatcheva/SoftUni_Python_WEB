from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('fruit/', include('fruits.urls')),
    path('profile/', include('profiles.urls')),
]
