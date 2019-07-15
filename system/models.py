from django.db import models

# Create your models here.
class Invoice(models.Model):
    number = models.CharField(max_length = 15)
    total = models.DecimalField(default=0.0,decimal_places=2,max_digits=25)
    date_created = models.DateTimeField('date_published')
    user_name =models.CharField(default='Grasp Chemicals',max_length = 25)
    order_number = models.CharField(default='0000000',max_length = 25)
    c_name =models.CharField(default=' ',max_length= 50)
    c_address = models.CharField(default=' ',max_length= 100)
    vat_number = models.CharField(default='00000',max_length = 25)
    vat = models.DecimalField(default=0.15,decimal_places=2,max_digits=2)
    def __str__(self):
        return "Invoice: "+ self.number + "\t Total: " +str(self.total) + " \tIssued  By: "+ self.user_name

class IProduct(models.Model):
    invoice = models.ForeignKey('Invoice',on_delete= models.CASCADE)
    p_name = models.CharField(max_length= 50)
    p_quantity = models.DecimalField(default=0.0,decimal_places=2,max_digits=25)
    p_price = models.DecimalField(default=0.0,decimal_places=2,max_digits=25)
    def __str__(self):
        return "Product : "+ self.p_name + " Quantity: " +str(object=self.p_quantity)+"Price: "+ str(self.p_price) +" Total: " + str(self.p_quantity +self.p_price)
class ICustomer(models.Model):
    invoice = models.ForeignKey('Invoice',on_delete= models.CASCADE)
    c_name =models.CharField(max_length= 50)
    c_address = models.CharField(max_length= 100)


    def __str__(self):
        return "Customer: "+ self.c_name + " Address: " +self.c_address
class IBankDetail(models.Model):
    b_name = models.CharField(max_length= 100)
    account_name = models.CharField(max_length= 100)
    accout_num = models.CharField(max_length= 25)
    account_type = models.CharField(max_length= 10)
    invoice = models.ForeignKey('Invoice',on_delete= models.CASCADE)

    def __str__(self):
        return "Bank: " + self.b_name + " Account No: "+ self.accout_num

class Quotation(models.Model):
    ref_number = models.CharField(max_length = 15)
    total = models.DecimalField(default=0.0,decimal_places=2,max_digits=25)
    customer = models.CharField(max_length = 50)
    customer_address = models.CharField(max_length = 50)
    user_name =models.CharField(default='Grasp Chemicals',max_length = 25)
    date_created = models.DateTimeField('date_published')

    def __str__(self):
        return "Quotation: "+ self.ref_number + "\t Total: " +str(self.total) + " \tIssued  By: "+ self.user_name +" Date created: "+ str(self.date_created)

class CProduct(models.Model):
    quotation = models.ForeignKey('Quotation',on_delete= models.CASCADE)
    p_name = models.CharField(max_length= 50)
    p_quantity = models.DecimalField(default=0.0,decimal_places=2,max_digits=25)
    p_price = models.DecimalField(default=0.0,decimal_places=2,max_digits=25)
    def __str__(self):
        return "Product : "+ self.p_name + " Quantity: " +str(object=self.p_quantity)+"Price: "+ str(self.p_price) +" Total: " + str(self.p_quantity +self.p_price)

class Delivery(models.Model):
    total = models.DecimalField(default=0.0,decimal_places=2,max_digits=25)
    customer = models.CharField(max_length = 50)
    customer_address = models.CharField(max_length = 50)
    user_name =models.CharField(default='Grasp Chemicals',max_length = 25)
    date_created = models.DateTimeField('date_published')
    vat_as_per_invoice = models.DecimalField(default=0.15,decimal_places=2,max_digits=2)
    def __str__(self):
        return "Delivery Note: "+ str(self.id) + "\t Total: " +str(self.total) + " \tIssued  By: "+ self.user_name +" Date created: "+ str(self.date_created)


class DProduct(models.Model):
    quotation = models.ForeignKey('Delivery',on_delete= models.CASCADE)
    p_name = models.CharField(max_length= 50)
    p_quantity = models.DecimalField(default=0.0,decimal_places=2,max_digits=25)
    p_price = models.DecimalField(default=0.0,decimal_places=2,max_digits=25)
    def __str__(self):
        return "Product : "+ self.p_name + " Quantity: " +str(object=self.p_quantity)+"Price: "+ str(self.p_price) +" Total: " + str(self.p_quantity +self.p_price)
