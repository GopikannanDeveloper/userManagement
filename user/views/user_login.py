from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers.login_serializer import UserLoginSerializer
from user.models.user_model import CustomUser
from common.Exceptions.custom_response import valid_response, valid_data_response
from rest_framework import status

class UserLoginView(APIView):
    def get(self, request):
        return Response("GET Method")
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return valid_response(detail="Login Successful", status_code=status.HTTP_200_OK)
        else:
            error = [f"{field} {error}" for field, errors in serializer.errors.items() for error in errors][0]
            return valid_response(detail=error, status_code=status.HTTP_400_BAD_REQUEST)
