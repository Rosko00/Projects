from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path ("anketa/", include ("anketa.urls")),
    path ("admin/", admin.site.urls),
]
