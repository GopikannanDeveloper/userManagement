import django_filters
from expense_tracking_app.models import ExpenseModel
from datetime import datetime, timedelta
from django.utils import timezone

class ExpenseFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')
    today = django_filters.BooleanFilter(method='filter_today')
    this_week = django_filters.BooleanFilter(method='filter_this_week')
    this_month = django_filters.BooleanFilter(method='filter_this_month')
    this_year = django_filters.BooleanFilter(method='filter_this_year')


    class Meta:
        model = ExpenseModel
        fields = ['start_date', 'end_date']

    def filter_today(self, queryset, name, value):
        if value:
            today = timezone.now().date()
            return queryset.filter(created_at__date=today)
        return queryset


    def filter_this_week(self, queryset, name, value):
        if value:
            start_of_week = timezone.now().date() - timedelta(days=timezone.now().date().weekday())
            end_of_week = start_of_week + timedelta(days=6)
            return queryset.filter(created_at__date__range=[start_of_week, end_of_week])
        return queryset


    def filter_this_month(self, queryset, name, value):
        if value:
            today = timezone.now().date()
            start_of_month = today.replace(day=1)
            end_of_month = start_of_month.replace(day=timezone.now().date().day)
            return queryset.filter(created_at__date__range=[start_of_month, end_of_month])
        return queryset

    
    def filter_this_year(self, queryset, name, value):
        if value:
            today = timezone.now().date()
            start_of_year = today.replace(month=1, day=1)
            end_of_year = start_of_year.replace(month=12, day=31)
            return queryset.filter(created_at__date__range=[start_of_year, end_of_year])
        return queryset
