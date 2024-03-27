from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers.login_serializer import UserLoginSerializer 
from user.serializers.signup_serializer import UserSignupSerializer 

from user.models.user_model import CustomUser
from common.Exceptions.custom_response import valid_response, valid_data_response
from rest_framework import status

class UserLoginView(APIView):
    def get(self, request):
        return Response("GET Method")
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return valid_response(detail="Login Successful", status_code=status.HTTP_200_OK)
        else:
            error = [f"{field} {error}" for field, errors in serializer.errors.items() for error in errors][0]
            return valid_response(detail=error, status_code=status.HTTP_400_BAD_REQUEST)

class UserSignupView(APIView):
    
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return valid_response(detail="Signup Successful", status_code=status.HTTP_201_CREATED)
        else:
            error = [f"{field} {error}" for field, errors in serializer.errors.items() for error in errors][0]
            return valid_response(detail=error, status_code=status.HTTP_400_BAD_REQUEST)
