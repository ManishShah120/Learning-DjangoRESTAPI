from django.contrib import admin
from django.urls import path
from api.views import student_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', student_api),
    path('studentapi/<int:pk>', student_api)
]
