from rest_framework import serializers
from django.contrib.auth import authenticate
from common.Exceptions.custom_exception import CustomException
from rest_framework import status
from user.models.user_model import CustomUser
from django.contrib.auth import get_user_model
# CustomUser = get_user_model()


class UserSignupSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=15)
    class Meta:
        model = CustomUser
        fields = ['email','name','password']

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise CustomException(detail="A user with that email already exists.", status_code=409)
        return value
    
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)