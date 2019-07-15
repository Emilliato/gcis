from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from  .models import Invoice ,Quotation,Delivery
from .forms import InvoiceForm,DetailsForm,BankDetailsForm,IProductForm ,QuotationForm,CProductForm, DeliveryForm,DProductForm
import random
from django.utils import timezone
from datetime import datetime
def developer(request):
    return HttpResponse('www.simpledeveloper.cf')
# Create your views here.
def index(request):
    template= 'system/index.html'
    invoice_list= Invoice.objects.order_by('-date_created')
    quotation_list= Quotation.objects.order_by('-date_created')
    delivery_list= Delivery.objects.order_by('-date_created')
    return render(request,template,{'invoice_list':invoice_list[:5],'mUser':request.user, 'quotation_list':quotation_list[:5], 'delivery_list':delivery_list[:5]})

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
    id=str(0)
    if(len(invoice_list)!=0):
        id = str(int(invoice_list[0].number[-1])+1)

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
def create_invoice(request):
    invoice_list = Invoice.objects.order_by('-date_created')
    id=0
    if(len(invoice_list)!=0):
        id = str(int(invoice_list[0].number[-1])+1)

    date1= datetime.strftime(timezone.now(),'%y')+str(str(random.randint(0,9)))+datetime.strftime(timezone.now(),'%d').lstrip('0')+id
    invoiceNum = 'GC'+date1
    if request.POST:
        order = request.POST['order_number']
        vat_number1 = request.POST['vat_number']
        vat1 = request.POST['vat']
        Invoice.objects.create(
            number= invoiceNum,
            date_created = timezone.now(),
            order_number = order,
            vat_number = vat_number1,
            vat = vat1
        )
        return  HttpResponseRedirect('/system/invoices/')

def add_details(request,invoice_id):
    a = get_object_or_404(Invoice,pk=invoice_id)
    id = invoice_id
    template= 'system/invoices/add_details.html'
    if request.POST:
        form1 = BankDetailsForm(request.POST)
        if form1.is_valid():
            f1 = form1.save(commit=False)
            f1.invoice = a
            f1.save(True)
            a2= get_object_or_404(Invoice,pk=invoice_id)
            return HttpResponseRedirect('/system/invoices/preview/%s'%a2.pk)

    else:
        form1 = BankDetailsForm()
    return render(request,template, {'form1':form1, 'id':id})
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
#for delivery notes
def deliveries(request):
        delivery_list= Delivery.objects.order_by('-date_created')
        template= 'system/deliveries/deliveries.html'
        return render(request,template,{'delivery_list':delivery_list})

def new_dnote(request):
    template= 'system/deliveries/new_delivery.html'
    if request.POST:
        form = DeliveryForm(request.POST)
        if form.is_valid():
            f= form.save(commit=False)
            f.user_name = request.user
            f.date_created = timezone.now()
            f.save(True)
            return HttpResponseRedirect('/system/deliveries/')
    else:
        form = DeliveryForm()
    return render(request,template, {'form':form})
def d_preview(request,i_id):
    delivery = get_object_or_404(Delivery,pk=i_id)
    a = delivery
    count = float(0.00)
    for c in delivery.dproduct_set.all():
        count = count + float(c.p_price*c.p_quantity)
    a.total = count
    a.save()
    template= 'system/deliveries/preview.html'
    context = {'delivery': a}
    return render(request,template,context)
def dadd_product(request,invoice_id):
    a = get_object_or_404(Delivery,pk=invoice_id)
    id = invoice_id
    template= 'system/deliveries/add_product.html'
    if request.POST:
        form = DProductForm(request.POST)
        if form.is_valid():
            f= form.save(commit=False)
            f.quotation = a
            f.save(True)
            a2= get_object_or_404(Delivery,pk=invoice_id)
            return HttpResponseRedirect('/system/deliveries/%s'%a2.pk+'/preview/')
    else:
        form = DProductForm()
    return  render(request,template,{'form':form, 'id':id})
def d_detail(request,i_id):
    delivery = get_object_or_404(Delivery,pk=i_id)
    a = delivery
    count = float(0.00)
    for c in delivery.dproduct_set.all():
        count = count + float(c.p_price*c.p_quantity)
    a.total = count
    a.save()
    template= 'system/deliveries/detail.html'
    context = {'delivery': a}
    return render(request,template,context)
