from rest_framework import serializers
from expense_app.models import CategoryModel
from common.Exceptions.custom_exception import CustomException
from rest_framework import status

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'