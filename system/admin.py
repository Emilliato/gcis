from django.contrib import admin
from .models import Invoice,IProduct,ICustomer,IBankDetail
# Register your models here.
class IProductInline(admin.TabularInline):
    model = IProduct
    
class ICustomerInline(admin.TabularInline):
    model = ICustomer

class IBankDetailInline(admin.TabularInline):
    model = IBankDetail

class InvoiceAdmin(admin.ModelAdmin):
    fields = ['number',]
    inlines = [IProductInline,ICustomerInline,IBankDetailInline]

admin.site.register(Invoice,InvoiceAdmin)
