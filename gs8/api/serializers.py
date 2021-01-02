from rest_framework import serializers
from .models import Student

# Validators Concepts
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should Start with R')


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[starts_with_r]) # When you have to apply validator to a specific field
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

    # Field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seats Full")
        return value

    # # Object level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data
