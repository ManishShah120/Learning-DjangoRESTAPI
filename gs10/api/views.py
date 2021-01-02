from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == "GET":
        id = request.data.get('id') 
        # If a single object is requested with id
        if id is not None:
            stu = Student.objects.get(id=id)
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
            return Response(res)

    if request.method == "PUT":
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True) # For updating a partial Field, incase you want to know how to update all the fields look at gs8        

        if serializer.is_valid():
            serializer.save()
            res = {'Message': 'Data Updated Successfully'}
            return Response(res)

        return Response(serializer.errors)

    if request.method == "DELETE":
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        res = {'Message': 'Data Deleted Successfully'}
        return Response(res)
