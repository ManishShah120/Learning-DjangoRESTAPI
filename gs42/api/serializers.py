from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'url', 'name', 'roll', 'city']
