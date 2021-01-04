from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', views.StudentList.as_view()),
    # path('studentapi/<int:pk>', views.StudentRetrieve.as_view()),
    path('studentapi/<int:pk>', views.StudentDestroy.as_view()),
    # path('studentapi/<int:pk>', StudentRetrieve.as_view()),

]
