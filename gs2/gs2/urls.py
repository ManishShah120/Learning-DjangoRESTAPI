from django.contrib import admin
from django.urls import path
from api.views import student_create

urlpatterns = [
    path("admin/", admin.site.urls),
    path("stucreate/", student_create),
]
