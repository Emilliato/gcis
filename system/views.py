from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from  .models import Invoice ,Quotation
from .forms import InvoiceForm,DetailsForm,BankDetailsForm,IProductForm ,QuotationForm,CProductForm
import random
from django.utils import timezone
from datetime import datetime
# Create your views here.
def index(request):
    template= 'system/index.html'
    invoice_list= Invoice.objects.order_by('-date_created')
    quotation_list= Quotation.objects.order_by('-date_created')
    return render(request,template,{'invoice_list':invoice_list[:5],'mUser':request.user, 'quotation_list':quotation_list[:5]})

#For invoices
def invoices(request):
    invoice_list= Invoice.objects.order_by('-date_created')
    template= 'system/invoices/invoices.html'
    return render(request,template,{'invoice_list':invoice_list,'mUser':request.user})
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
def new(request):
    invoice_list = Invoice.objects.order_by('-date_created')
    id=0
    if(len(invoice_list)!=0):
        id = str(int(invoice_list[0].number[-1])+str(1))

    date1= datetime.strftime(timezone.now(),'%y')+str(str(random.randint(0,9)))+datetime.strftime(timezone.now(),'%d').lstrip('0')+id
    invoiceNum = 'GC'+date1
    template= 'system/invoices/new_invoice.html'
    if request.POST:
        form = InvoiceForm(request.POST)
        if form.is_valid():
            f= form.save(commit=False)
            f.number = invoiceNum
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


#for quotation
def quotations(request):
        quotation_list= Quotation.objects.order_by('-date_created')
        template= 'system/quotations/quotations.html'
        return render(request,template,{'quotation_list':quotation_list})
def new_quote(request):
    template= 'system/quotations/new_quotation.html'
    if request.POST:
        form = QuotationForm(request.POST)
        if form.is_valid():
            f= form.save(commit=False)
            f.user_name = request.user
            f.date_created = timezone.now()
            f.save(True)
            return HttpResponseRedirect('/system/quotations/')
    else:
        form = QuotationForm()
    return render(request,template, {'form':form})
def qadd_product(request,invoice_id):
    a = get_object_or_404(Quotation,pk=invoice_id)
    id = invoice_id
    template= 'system/quotations/add_product.html'
    if request.POST:
        form = CProductForm(request.POST)
        if form.is_valid():
            f= form.save(commit=False)
            f.quotation = a
            f.save(True)
            a2= get_object_or_404(Quotation,pk=invoice_id)
            return HttpResponseRedirect('/system/quotations/%s'%a2.pk+'/preview/')
    else:
        form = CProductForm()
    return  render(request,template,{'form':form, 'id':id})
def q_preview(request,i_id):
    quotation = get_object_or_404(Quotation,pk=i_id)
    a = quotation
    count = float(0.00)
    for c in quotation.cproduct_set.all():
        count = count + float(c.p_price*c.p_quantity)
    a.total = count
    a.save()
    template= 'system/quotations/preview.html'
    context = {'quotation': a}
    return render(request,template,context)
def q_detail(request,i_id):
    quotation = get_object_or_404(Quotation,pk=i_id)
    a = quotation
    count = float(0.00)
    for c in quotation.cproduct_set.all():
        count = count + float(c.p_price*c.p_quantity)
    a.total = count
    a.save()
    template= 'system/quotations/detail.html'
    context = {'quotation': a}
    return render(request,template,context)

#for sales reciepts can be changed to delivery notes
def reciepts(response):
    return HttpResponse("Welcome to the reciepts section.")
