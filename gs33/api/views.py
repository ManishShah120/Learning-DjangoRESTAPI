from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Writting a simple function which will return only those data whose passy value is equal to the username
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)
