from rest_framework import serializers

# One Way
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'
