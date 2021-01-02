from django.contrib import admin
from django.urls import path
from api.views import SudentAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', SudentAPI.as_view()),
    path('studentapi/<int:pk>', SudentAPI.as_view())
]
