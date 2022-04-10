from Api import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    # Gestion get/create/delete with all books
    url(r'^api/$', views.book_list),
    # Gestion get/update/delete with one specific book
    url(r'^api/(?P<pk>[0-9]+)$', views.book_detail),
]
