from rest_framework import serializers
from django.contrib.auth import authenticate
from common.Exceptions.custom_exception import CustomException
from rest_framework import status

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email,
                                password=password)

            if not user:
                raise CustomException(detail='Invalid email or password',status_code=status.HTTP_400_BAD_REQUEST)
        else:
            raise CustomException(detail='Must include "email" and "password"',status_code=status.HTTP_404_NOT_FOUND)

        attrs['user'] = user
        return attrs
