from django.urls import path
from user.views.user_login import UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view(),name="login"),
]