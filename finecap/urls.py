from django.urls import path
from core.views import index
from django.contrib import admin


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls)
]
