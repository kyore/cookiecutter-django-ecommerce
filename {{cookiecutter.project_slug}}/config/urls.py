from django.apps import apps
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(apps.get_app_config('oscar').urls[0])),
    path('admin/', admin.site.urls),
]
