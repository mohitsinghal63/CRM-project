from crm_main.CRM import models
from crm_main.CRM.models import Customer, Query1, Detail

customers = Customer.objects.all()

firstCustomer = Customer.objects.first()

lastCustomer = Customer.objects.last()

customerByName = Customer.objects.get(name='Peter Piper')

customerById = Customer.objects.get(id=4)

firstCustomer.Query1_set.all()

querys = Query1.objects.first()
parentName = querys.customer.name

Details = Detail.objects.filter(category="OUTBOUND")

leastToGreatest = Detail.objects.all().query_by('id')
greatestToLeast = Detail.objects.all().query_by('-id')

DetailsFiltered = Detail.objects.filter(Remark__name="urgent")

xyzQueries = firstCustomer.querys_set.filter(Detail__name="XYZ").count()

allQuery1 = {}

for querys in firstCustomer.order_set.all():
    if querys.Detail.name in allQuery1:
        allQuery1[querys.Detail.name] += 1
    else:
        allQuery1[querys.detail.name] = 1


class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)


class ChildModel(models.Model):
    parent = models.ForeignKey(Customer)
    name = models.CharField(max_length=200, null=True)


parent = ParentModel.objects.first()

parent.childmodel_set.all()



