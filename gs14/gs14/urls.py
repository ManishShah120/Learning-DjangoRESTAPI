from django.contrib import admin
from django.urls import path
from api.views import LCStudentAPI, RUDStudentAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', LCStudentAPI.as_view()),
    path('studentapi/<int:pk>', RUDStudentAPI.as_view()),
]
