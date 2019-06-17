from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from  .models import Invoice
from .forms import InvoiceForm,DetailsForm,BankDetailsForm,IProductForm
import random
from django.utils import timezone
# Create your views here.
def index(request):
    template= loader.get_template('system/index.html')

    return HttpResponse(template.render({},request))
def invoices(request):
    invoice_list= Invoice.objects.order_by('date_created')
    template= 'system/invoices/invoices.html'
    return render(request,template,{'invoice_list':invoice_list})

def purchases(response):
    return HttpResponse("Welcome to the purchases section.")
def quotations(response):
    return HttpResponse("Welcome to the quotations section.")
def reciepts(response):
    return HttpResponse("Welcome to the reciepts section.")

def new(request):
    template= 'system/invoices/new_invoice.html'
    if request.POST:
        form = InvoiceForm(request.POST)
        if form.is_valid():
            f= form.save(commit=False)
            f.number = str(random.randint(0,1000))
            f.date_created = timezone.now()
            f.save(True)
            return HttpResponseRedirect('/system/invoices/')

    else:
        form = InvoiceForm()
    return render(request,template, {'form':form})

def add_details(request,invoice_id):
    a = get_object_or_404(Invoice,pk=invoice_id)
    id = invoice_id
    template= 'system/invoices/add_details.html'
    template2= 'system/invoices/preview.html'
    if request.POST:
        form = DetailsForm(request.POST)
        form1 = BankDetailsForm(request.POST)
        if form.is_valid() and form1.is_valid():
            f = form.save(commit=False)
            f.invoice = a
            f.save(True)

            f1 = form1.save(commit=False)
            f1.invoice = a
            f1.save(True)
            a2= get_object_or_404(Invoice,pk=invoice_id)
            return HttpResponseRedirect('/system/invoices/preview/%s'%a2.pk)

    else:
        form = DetailsForm()
        form1 = BankDetailsForm()
    return render(request,template, {'form':form,'form1':form1, 'id':id})
def add_product(request,invoice_id):
    a = get_object_or_404(Invoice,pk=invoice_id)
    id = invoice_id
    template= 'system/invoices/add_product.html'
    template1= 'system/invoices/preview.html'
    if request.POST:
        form = IProductForm(request.POST)
        if form.is_valid():
            f= form.save(commit=False)
            f.invoice = a
            f.save(True)
            a2= get_object_or_404(Invoice,pk=invoice_id)
            return HttpResponseRedirect('/system/invoices/preview/%s'%a2.pk)
    else:
        form = IProductForm()
    return  render(request,template,{'form':form, 'id':id})


def i_detail(request,i_id):
    invoice = get_object_or_404(Invoice,pk=i_id)
    a = invoice
    count = float(0.00)
    for c in invoice.iproduct_set.all():
        count = count + float(c.p_price*c.p_quantity)
    a.total = count
    a.save()

    template= 'system/invoices/detail.html'
    context = {'invoice': a}
    return render(request,template,context)
def i_preview(request,i_id):
    invoice = get_object_or_404(Invoice,pk=i_id)
    a = invoice
    count = float(0.00)
    for c in invoice.iproduct_set.all():
        count = count + float(c.p_price*c.p_quantity)
    a.total = count
    a.save()
    template= 'system/invoices/preview.html'
    context = {'invoice': a}
    return render(request,template,context)
