from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request, pk=None):
    if request.method == "GET":
        # If a single object is requested with id
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        # If no id is provided then all the object/instance will be returned
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'Message': 'Data Created Successfully'}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT": # Is used for Complete Update
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'Message': 'Data Updated Successfully'}
            return Response(res)
        return Response(serializer.errors)
    
    if request.method == "PATCH": # Is used for Partial Update
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'Message': 'Partial Data Updated Successfully'}
            return Response(res)
        return Response(serializer.errors)

    if request.method == "DELETE":
        stu = Student.objects.get(id=pk)
        stu.delete()
        res = {'Message': 'Data Deleted Successfully'}
        return Response(res)
