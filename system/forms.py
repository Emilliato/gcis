from django import forms
from .models import Invoice, IProduct, ICustomer,IBankDetail,Quotation, CProduct

class InvoiceForm(forms.ModelForm):
    class Meta:
        model =Invoice
        fields =('order_number','vat_number','vat')
class QuotationForm(forms.ModelForm):
    class Meta:
        model =Quotation
        fields =('customer','customer_address','ref_number')

class IProductForm(forms.ModelForm):
    class Meta:
        model =IProduct
        fields =('p_name','p_quantity','p_price')
class CProductForm(forms.ModelForm):
    class Meta:
        model =CProduct
        fields =('p_name','p_quantity','p_price')
class DetailsForm(forms.ModelForm):
    class Meta:
        model =ICustomer
        fields =('c_name','c_address')
class BankDetailsForm(forms.ModelForm):
    class Meta:
        model =IBankDetail
        fields =('b_name','account_name','accout_num','account_type')
