from rest_framework.exceptions import APIException

class CustomException(APIException):
    def __init__(self, detail=None, status_code=None):
        if detail is not None:
            self.detail = detail
        if status_code is not None:
            self.status_code = status_code
    
    def __str__(self):
        return self.detail
    