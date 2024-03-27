from django.contrib import admin
from expense_tracking_app.models import CategoryModel
from expense_tracking_app.models import ExpenseModel

# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(ExpenseModel)

