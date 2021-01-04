from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from rest_framework.filters import OrderingFilter

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name'] # If not provided then all the fieds get the ordering options
    ordering_fields = ['name', 'city'] # If not provided then all the fieds get the ordering options