from django.db import models
from user.models.user_model import CustomUser
from expense_tracking_app.models.category_model import CategoryModel
from django.utils import timezone

class ExpenseModel(models.Model):
    expense_id = models.AutoField(primary_key=True)
    expense_name = models.CharField(max_length=100)
    expense_category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING)
    expense = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    created_user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "expense"

    def __str__(self):
        return f"{self.expense_name}"
