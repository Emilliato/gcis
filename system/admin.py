from django.contrib import admin
from .models import Invoice,IProduct,ICustomer,IBankDetail,Quotation,CProduct, Delivery, DProduct
# Register your models here.
class IProductInline(admin.TabularInline):
    model = IProduct
class DProductInline(admin.TabularInline):
    model = DProduct
class CProductInline(admin.TabularInline):
    model = CProduct
class ICustomerInline(admin.TabularInline):
    model = ICustomer

class IBankDetailInline(admin.TabularInline):
    model = IBankDetail

class InvoiceAdmin(admin.ModelAdmin):
    fields = ['number',]
    inlines = [IProductInline,ICustomerInline,IBankDetailInline]

class QuotationAdmin(admin.ModelAdmin):
    fields = ['customer','customer_address','ref_number','date_created',]
    inlines = [CProductInline]
class DeliveryAdmin(admin.ModelAdmin):
    fields = ['customer','customer_address',]
    inlines = [DProductInline]
admin.site.register(Invoice,InvoiceAdmin)
admin.site.register(Quotation,QuotationAdmin)
admin.site.register(Delivery,DeliveryAdmin)
