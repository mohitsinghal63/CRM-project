from django.forms import ModelForm
from .models import Customer, Query1

class OrderForm(ModelForm):
	class Meta:
		model = Query1
		fields = '__all__'