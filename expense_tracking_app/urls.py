from django.urls import path
from expense_tracking_app.views.category_view import CategoryAPIView
from expense_tracking_app.views.expense_view import ExpenseAPIView


urlpatterns = [
    path('category/', CategoryAPIView.as_view(),name="login"),
    path('category/<int:category_id>/', CategoryAPIView.as_view(), name='category-update'),
    path('expense/', ExpenseAPIView.as_view(),name="signup"),
    
]