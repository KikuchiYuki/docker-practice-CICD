from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mytodo.urls")), # mytodo/urls.pyを参照
]