from rest_framework import serializers
from expense_app.models import ExpenseModel
from common.Exceptions.custom_exception import CustomException
from rest_framework import status

class ExpenseSerializer(serializers.Serializer):
    class Meta:
        model = ExpenseModel
        fields = '__all__'