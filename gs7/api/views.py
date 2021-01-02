import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Class based View
@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)

            id = pythondata.get('id', None)
            
            if id is not None:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')

            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)

            serializer = StudentSerializer(data = pythondata)
            
            if serializer.is_valid():
                serializer.save()
                res = {'Message': 'Data Created Successfully'}
                # json_data = JSONRenderer().render(res)
                # return HttpResponse(json_data, content_type='application/json')
                return JsonResponse(res, safe=False)

            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')        

    def put(self, request, *args, **kwargs):
        if request.method == "PUT":
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            
            id = pythondata.get('id')
            stu = Student.objects.get(id=id)
            
            # complete Update - All data required
            # serializer = StudentSerializer(stu, data=pythondata)
            
            # Partial Update - All data not required
            serializer = StudentSerializer(stu, data=pythondata, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                res = {'Message': 'Data Updated Successfully'}
                # json_data = JSONRenderer().render(res)
                # return HttpResponse(json_data, content_type='application/json')
                return JsonResponse(res, safe=False)

            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        if request.method == "DELETE":
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)

            id = pythondata.get('id')
            stu = Student.objects.get(id=id)
            stu.delete()
            res = {'Message': 'Data Deleted Successfully'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(res, safe=False)













# # Create your views here.
# # Funcation Based View
# # @csrf_exempt
# def student_api(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)

#         id = pythondata.get('id', None)
        
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')

#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')


#     if request.method == "POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)

#         serializer = StudentSerializer(data = pythondata)
        
#         if serializer.is_valid():
#             serializer.save()
#             res = {'Message': 'Data Created Successfully'}
#             # json_data = JSONRenderer().render(res)
#             # return HttpResponse(json_data, content_type='application/json')
#             return JsonResponse(res, safe=False)

#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')


#     if request.method == "PUT":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
        
#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)
        
#         # complete Update - All data required
#         # serializer = StudentSerializer(stu, data=pythondata)
        
#         # Partial Update - All data not required
#         serializer = StudentSerializer(stu, data=pythondata, partial=True)
        
#         if serializer.is_valid():
#             serializer.save()
#             res = {'Message': 'Data Updated Successfully'}
#             # json_data = JSONRenderer().render(res)
#             # return HttpResponse(json_data, content_type='application/json')
#             return JsonResponse(res, safe=False)

#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')


#     if request.method == "DELETE":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)

#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         res = {'Message': 'Data Deleted Successfully'}
#         # json_data = JSONRenderer().render(res)
#         # return HttpResponse(json_data, content_type='application/json')
#         return JsonResponse(res, safe=False)

 
