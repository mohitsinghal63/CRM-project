from django.contrib import admin


from .models import Customer, Query1, Detail, Remark
admin.site.register(Customer)
admin.site.register(Query1)
admin.site.register(Detail)
admin.site.register(Remark)