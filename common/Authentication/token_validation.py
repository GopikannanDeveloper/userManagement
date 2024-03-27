import jwt
from datetime import datetime, timedelta
from django.conf import settings
from user.models.user_model import CustomUser
from common.Exceptions.custom_exception import CustomException
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status

class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.headers.get('Authorization')
            if not token:
                raise CustomException(detail='Token Not Found', status_code=status.HTTP_401_UNAUTHORIZED)
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']
            user = CustomUser.objects.get(pk=user_id)
            return (user, token)
        
        except jwt.ExpiredSignatureError:
            raise CustomException(detail='Token Expired', status_code=status.HTTP_401_UNAUTHORIZED)
        except jwt.InvalidTokenError:
            raise CustomException(detail='Invalid Token', status_code=status.HTTP_401_UNAUTHORIZED)
        except CustomUser.DoesNotExist:
            raise CustomException(detail='User Not Found', status_code=status.HTTP_401_UNAUTHORIZED)
        