
from django.urls import path
from . import views
app_name = 'system'
urlpatterns = [
    path('', views.index, name='index'),
    path('invoices/', views.invoices, name='invoices'),
    #create /system/invoices/create
    path('invoices/newinvoice/', views.new, name='icreate'),
    #add details
    path('invoices/<int:invoice_id>/add_details', views.add_details, name='add_details'),

    path('invoices/<int:invoice_id>/add_product', views.add_product, name='add_product'),
    #detail /system/invoices/2/
    path('invoices/<int:i_id>/', views.i_detail, name='idetail'),
    #preview /system/invoices/2/preview
    path('invoices/preview/<int:i_id>/', views.i_preview, name='ipreview'),


    #Quotations
    path('quotations/', views.quotations, name='quotations'),
    #create /system/quotations/create
    path('quotations/create/', views.new_quote, name='qcreate'),
    #add products
    path('quotations/<int:invoice_id>/add_product', views.qadd_product, name='qadd_product'),
    #preview /system/quotations/2/preview
    path('quotations/<int:i_id>/preview/', views.q_preview, name='qpreview'),
    #detail /system/quotations/2/
    path('quotations/<int:i_id>/', views.q_detail, name='qdetail'),

    path('purchases/', views.index, name='purchases'),
    path('reciepts/', views.reciepts, name='reciepts'),

]
