from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    roll = serializers.IntegerField()
    name = serializers.CharField(max_length=80)
    city = serializers.CharField(max_length=50)