from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def queries(self):
        query_count = self.query_set.all().count()
        return str(query_count)


class Remark(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Detail(models.Model):
    CATEGORY = (
        ('INBOUND', 'INBOUND'),
        ('OUTBOUND', 'OUTBOUND'),
        ('RETAIL', 'RETAIL'),
        ('NEW', 'NEW'),

    )
    Company_name = models.CharField(max_length=200, null=True)
    software_id = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # tags = models.ManyToManyField(Remark)
    def __str__(self):
        return self.name


class Query1(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('UNDER_PROGRESS', 'UNDER_PROGRESS'),
        ('TEAM_REVIEWING', 'TEAM_REVIEWING'),
        ('RESOLVED', 'RESOLVED'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    query_type = models.ForeignKey(Detail, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return str(self.detail)
