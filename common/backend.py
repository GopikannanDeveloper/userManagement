from django.contrib.auth import get_user_model
from common.Exceptions.custom_exception import CustomException
from rest_framework import status

class UserModelBackend(object):
    def authenticate(self, request, username=None, password=None):
        User = get_user_model()
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                if user.verified_user is False:
                    raise CustomException(detail='User is not activated',status_code=status.HTTP_400_BAD_REQUEST)
                return user
            
        except User.DoesNotExist:
            return None
