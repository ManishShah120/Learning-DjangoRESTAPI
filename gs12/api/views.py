from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView


class SudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        # If a single object is requested with id
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # If no id is provided then all the object/instance will be returned
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'Message': 'Data Created Successfully'}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'Message': 'Data Updated Successfully'}
            return Response(res, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def patch(self, request, pk, format=None):
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'Message': 'Partial Data Updated Successfully'}
            return Response(res, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        stu = Student.objects.get(id=pk)
        stu.delete()
        res = {'Message': 'Data Deleted Successfully'}
        return Response(res, status=status.HTTP_200_OK)
