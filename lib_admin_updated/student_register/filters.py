import django_filters
from .models import Student,Course
class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields="__all__"