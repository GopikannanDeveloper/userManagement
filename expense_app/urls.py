from django.urls import path
from expense_app.views.category_view import CategoryAPIView
from expense_app.views.expense_view import ExpenseAPIView


urlpatterns = [
    path('category/', CategoryAPIView.as_view(),name="login"),
    path('expense/', ExpenseAPIView.as_view(),name="signup"),
]