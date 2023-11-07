"""
encoding_django URL Configuration
"""
from django.contrib import admin
from django.urls import path
from core import current_datetime, render_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('current_datetime/', current_datetime),
    path('hello/', render_html)
]
