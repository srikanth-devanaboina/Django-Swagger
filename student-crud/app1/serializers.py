from rest_framework import serializers



class CreateStudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    mobile_number = serializers.IntegerField()



class UpdateStudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()