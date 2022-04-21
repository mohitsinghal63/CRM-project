import django_filters
from .models import *



class OrderFilter(django_filters.FilterSet):
	class Meta:
		model = Query1
		fields = '__all__'
		exclude = ['customer', 'date_created']