from django import forms
from .models import Invoice, IProduct, ICustomer,IBankDetail

class InvoiceForm(forms.ModelForm):
    class Meta:
        model =Invoice
        fields =('order_number','vat_number')

class IProductForm(forms.ModelForm):
    class Meta:
        model =IProduct
        fields =('p_code','p_name','p_quantity','p_price')
class DetailsForm(forms.ModelForm):
    class Meta:
        model =ICustomer
        fields =('c_name','c_address','c_person','c_mobile_n','c_tel')
class BankDetailsForm(forms.ModelForm):
    class Meta:
        model =IBankDetail
        fields =('b_name','account_name','accout_num','swift_code','sort_code','account_type')
