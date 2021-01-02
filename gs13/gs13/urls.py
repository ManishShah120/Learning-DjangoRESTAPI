from django.contrib import admin
from django.urls import path
from api.views import StudentList, StudentCreate, StudentRetrieve, StudentUpdate, StudentDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', StudentList.as_view()),
    path('studentapi/', StudentCreate.as_view()),
    # path('studentapi/<int:pk>', StudentRetrieve.as_view()),
    # path('studentapi/<int:pk>', StudentUpdate.as_view()),
    # path('studentapi/<int:pk>', StudentDestroy.as_view()),
]
