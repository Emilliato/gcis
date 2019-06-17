"""gcisystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
app_name = 'system'
urlpatterns = [
    path('', views.index, name='index'),
    path('invoices/', views.invoices, name='invoices'),
    path('quotations/', views.quotations, name='quotations'),
    path('purchases/', views.purchases, name='purchases'),
    path('reciepts/', views.reciepts, name='reciepts'),
    #create /system/invoices/create
    path('invoices/newinvoice/', views.new, name='icreate'),
    #add details
    path('invoices/<int:invoice_id>/add_details', views.add_details, name='add_details'),

    path('invoices/<int:invoice_id>/add_product', views.add_product, name='add_product'),
     #detail /system/invoices/2/
     path('invoices/<int:i_id>/', views.i_detail, name='idetail'),
     #preview /system/invoices/2/preview
     path('invoices/preview/<int:i_id>/', views.i_preview, name='ipreview'),
]
