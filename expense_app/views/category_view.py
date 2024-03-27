from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from expense_app.models import CategoryModel
from expense_app.serializers import CategorySerializer
from user.models.user_model import CustomUser
from common.Exceptions.custom_response import valid_response, valid_data_response


class CategoryAPIView(APIView):
    def get(self, request):
        categories = CategoryModel.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return valid_data_response(serializer.data, status_code=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.get(userid=2)
            serializer.save(created_user=user)
            return valid_data_response(serializer.data, status_code=status.HTTP_201_CREATED)
        else:
            error = [f"{field} {error}" for field, errors in serializer.errors.items() for error in errors][0]
            return valid_response(detail=error, status_code=status.HTTP_400_BAD_REQUEST)
    
    # def put(self, request):
    #     serializer = CategorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(created_user=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)