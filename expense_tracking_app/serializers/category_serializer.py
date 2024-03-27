from rest_framework import serializers
from expense_tracking_app.models import CategoryModel
from user.models.user_model import CustomUser
from common.Exceptions.custom_exception import CustomException
from rest_framework import status

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = '__all__'

    # def create(self, validated_data):
    #     data = CategoryModel.objects.filter(category_name=validated_data['category_name'], created_user=validated_data['created_user'])
    #     if data:
    #         raise CustomException(detail="Category Already Exist", status_code=status.HTTP_409_CONFLICT)
    #     return CategoryModel.objects.create(**validated_data)