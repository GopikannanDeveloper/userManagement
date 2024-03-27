from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from expense_tracking_app.models import CategoryModel
from expense_tracking_app.serializers import CategorySerializer
from user.models.user_model import CustomUser
from common.Exceptions.custom_response import valid_response, valid_data_response
# from common.Authentication.token_validation import TokenAuthentication


class CategoryAPIView(APIView):
    # authentication_classes = [TokenAuthentication]

    def get(self, request, category_id=None):
        if category_id:
            try:
                user = CustomUser.objects.get(userid=1)
                categories = CategoryModel.objects.filter(pk=category_id, created_user=user)
                serializer = CategorySerializer(categories, many=True)
                return valid_data_response(detail=serializer.data, status_code=status.HTTP_200_OK)
            except CategoryModel.DoesNotExist:
                return valid_response(detail="Category not found", status_code=status.HTTP_404_NOT_FOUND)
        
        categories = CategoryModel.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return valid_data_response(detail=serializer.data, status_code=status.HTTP_200_OK)

    def post(self, request):
        user = CustomUser.objects.get(userid=1)
        request.data['created_user'] = user.userid
        serializer = CategorySerializer(data=request.data)
        existing_category = CategoryModel.objects.filter(category_name=request.data['category_name'],created_user=user.userid) 
        if existing_category:
            return valid_response(detail="Category already exists", status_code=status.HTTP_409_CONFLICT)

        if serializer.is_valid():
            serializer.save()
            return valid_response(detail="Category Created Successfully", status_code=status.HTTP_201_CREATED)
        else:
            error = [f"{field} {error}" for field, errors in serializer.errors.items() for error in errors][0]
            return valid_response(detail=error, status_code=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, category_id=None):
        try:
            category = CategoryModel.objects.get(pk=category_id)
        except CategoryModel.DoesNotExist:
            return valid_response(detail="Category not found", status_code=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return valid_response(detail="Category updated successfully", status_code=status.HTTP_200_OK)
        else:
            error = [f"{field} {error}" for field, errors in serializer.errors.items() for error in errors][0]
            return valid_response(detail=error, status_code=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, category_id=None):
        try:
            user = CustomUser.objects.get(userid=1)
            category = CategoryModel.objects.get(pk=category_id, created_user=user)
            category.delete()
            return valid_response(detail="Category was deleted successfully", status_code=status.HTTP_200_OK)

        except CategoryModel.DoesNotExist:
            return valid_response(detail="Category not found", status_code=status.HTTP_404_NOT_FOUND)
           