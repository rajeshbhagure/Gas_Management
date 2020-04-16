from django.db import models

# Create your models here.


class PriceModel(models.Model):
    c_type=models.CharField(max_length=30)
    price=models.FloatField()
    # date=models.DateField()



class CustomerModel(models.Model):
    cust_no=models.IntegerField(primary_key=True)
    password=models.CharField(max_length=30)
    Cy_type=models.CharField(max_length=10)
    date_conn=models.DateField()
    name=models.CharField(max_length=30,unique=True)
    address=models.CharField(max_length=60)
    city=models.CharField(max_length=30)
    contact=models.IntegerField()
    pincode=models.IntegerField()




class Stockdetails(models.Model):
    s_date=models.DateTimeField()
    stock_comm=models.IntegerField()
    stock_dom = models.IntegerField()
    defective_comm=models.IntegerField()
    defective_dom=models.IntegerField()
    current_stock_comm=models.IntegerField()
    current_stock_dom=models.IntegerField()


class BillingModel(models.Model):
    b_id=models.IntegerField()
    cust_no=models.IntegerField(primary_key=True)
    cy_type=models.CharField(max_length=10)
    bk_date=models.DateTimeField()
    del_date=models.DateTimeField()
    amt=models.FloatField()



class TransactionModel(models.Model):
    Tid=models.IntegerField()
    customer_id=models.IntegerField(primary_key=True)
    cy_type=models.CharField(max_length=10)
    cust_name=models.CharField(max_length=30)
    datetime=models.DateTimeField()
    status=models.CharField(max_length=30)







