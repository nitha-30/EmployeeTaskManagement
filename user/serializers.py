from rest_framework import serializers
from user.models import User


class RegisterSerializer(serializers.Serializer):
    
    email = serializers.EmailField(max_length=120, required=True)
    password = serializers.CharField(max_length=128, required=True)
    name = serializers.CharField(max_length=150, required=True)
    phone_number = serializers.CharField(max_length=20, required=False)

    def to_internal_value(self, data):
    
        return super(RegisterSerializer, self).to_internal_value(data)
