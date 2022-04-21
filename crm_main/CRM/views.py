from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .filters import OrderFilter
from .forms import OrderForm


def dashboard(request):
    Query = Query1.objects.all().order_by('-status')[0:5]
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_queries = Query1.objects.all().count()
    pending = Query1.objects.filter(status='Pending').count()
    confirmed = Query1.objects.filter(status='Confirmed').count()
    progress = Query1.objects.filter(status='UNDER_PROGRESS').count()
    review = Query1.objects.filter(status='TEAM_REVIEWING').count()
    resolved = Query1.objects.filter(status='RESOLVED').count()

    context = {'query': Query, 'customers': customers, 'total_customers': total_customers,
               'total_queries': total_queries, 'pending': pending,
               'confirmed': confirmed, 'progress': progress, 'review': review, 'resolved': resolved}

    return render(request, 'CRM/dashboard.html', context)


def detail(request):
    detail = Detail.objects.all()
    context = {'detail':detail}

    return render(request, 'CRM/detail.html', {'detail': detail},context)


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    Query1 = customer.Query1_set.all()
    total_queries = Query1.count()
    orderFilter = OrderFilter(request.GET, queryset=Query1) 
    Query1 = orderFilter.qs
    context = {'customer':customer, 'Query1':Query1, 'total_queries':total_queries,'filter':orderFilter}
    return render(request, 'CRM/customer.html',context)



def createquery(request):
	action = 'create'
	form = OrderForm()
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {'action':action, 'form':form}
	return render(request, 'accounts/query_form.html', context)

#-------------------(UPDATE VIEWS) -------------------

def updatequery(request, pk):
	action = 'update'
	order = Query1.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/customer/' + str(order.customer.id))

	context =  {'action':action, 'form':form}
	return render(request, 'accounts/query_form.html', context)

#-------------------(DELETE VIEWS) -------------------

def deletequery(request, pk):
	order = Query1.objects.get(id=pk)
	if request.method == 'POST':
		customer_id = order.customer.id
		customer_url = '/customer/' + str(customer_id)
		order.delete()
		return redirect(customer_url)
		
	return render(request, 'accounts/delete_query.html', {'item':order})
