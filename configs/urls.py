"""
encoding_django URL Configuration
"""
from django.contrib import admin
from django.urls import path
from core.views import current_datetime

urlpatterns = [
    path('admin/', admin.site.urls),
    path('current_datetime/', current_datetime)
]
