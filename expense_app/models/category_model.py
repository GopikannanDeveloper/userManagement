from django.db import models
from user.models.user_model import CustomUser

class CategoryModel(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "category"

    def __str__(self):
        return f"{self.category_name}"
