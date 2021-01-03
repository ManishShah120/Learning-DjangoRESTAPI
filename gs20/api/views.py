from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # For single and specific class
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser] # For in use only for those User whose IsStaff = True
    # The Above portion can also be implemented for multiple classes having the saame permission by writting the some code in the settings.py file.
