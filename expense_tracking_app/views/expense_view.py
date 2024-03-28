from rest_framework.views import APIView
from rest_framework import status
from expense_tracking_app.models import ExpenseModel
from expense_tracking_app.serializers import ExpenseSerializer
from user.models.user_model import CustomUser
from common.Exceptions.custom_response import valid_response, valid_data_response
from common.Authentication.token_validation import TokenAuthentication
from expense_tracking_app.filters.expense_filter import ExpenseFilter

class ExpenseAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    def get(self, request, expense_id=None):
        authenticated_user = request.user
        expense_filter = ExpenseFilter(request.GET, queryset=ExpenseModel.objects.filter(created_user=authenticated_user))
        if expense_id:
            try:
                categories = ExpenseModel.objects.filter(pk=expense_id, created_user=authenticated_user)
                serializer = ExpenseSerializer(categories, many=True)
                return valid_data_response(detail=serializer.data, status_code=status.HTTP_200_OK)
            except ExpenseModel.DoesNotExist:
                return valid_response(detail="Expense was not found", status_code=status.HTTP_404_NOT_FOUND)
        
        # categories = ExpenseModel.objects.filter(created_user=authenticated_user)
        serializer = serializer = ExpenseSerializer(expense_filter.qs, many=True)
        return valid_data_response(detail=serializer.data, status_code=status.HTTP_200_OK)

    def post(self, request):
        request.data['created_user'] = request.user.userid
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return valid_response(detail="Expense was Created Successfully", status_code=status.HTTP_201_CREATED)
        else:
            error = [f"{field} {error}" for field, errors in serializer.errors.items() for error in errors][0]
            return valid_response(detail=error, status_code=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, expense_id=None):
        try:
            category = ExpenseModel.objects.get(pk=expense_id)
        except ExpenseModel.DoesNotExist:
            return valid_response(detail="Expense was not found", status_code=status.HTTP_404_NOT_FOUND)

        serializer = ExpenseSerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return valid_response(detail="Expense was updated successfully", status_code=status.HTTP_200_OK)
        else:
            error = [f"{field} {error}" for field, errors in serializer.errors.items() for error in errors][0]
            return valid_response(detail=error, status_code=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, expense_id=None):
        authenticated_user = request.user.userid
        try:
            user = CustomUser.objects.get(userid=authenticated_user)
            category = ExpenseModel.objects.get(pk=expense_id, created_user=user)
            category.delete()
            return valid_response(detail="Expense was deleted successfully", status_code=status.HTTP_200_OK)

        except ExpenseModel.DoesNotExist:
            return valid_response(detail="Expense was not found", status_code=status.HTTP_404_NOT_FOUND)