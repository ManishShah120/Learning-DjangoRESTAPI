from django.contrib import admin
from django.urls import path
from api.views import (
    student_detail,
    student_list,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("stuinfo/<int:pk>", student_detail),
    path("stuinfo/", student_list),
]
