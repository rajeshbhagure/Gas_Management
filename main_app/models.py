from django.db import models

# Create your models here.











# class BillingModel(models.Model):
#     b_id=models.IntegerField()
#     cust_no=models.IntegerField(primary_key=True)
#     cy_type=models.CharField(max_length=10)
#     bk_date=models.DateTimeField()
#     del_date=models.DateTimeField()
#     amt=models.FloatField()



class TransactionModel(models.Model):
    Tid=models.IntegerField()
    customer_id=models.IntegerField(primary_key=True)
    cy_type=models.CharField(max_length=10)
    cust_name=models.CharField(max_length=30)
    datetime=models.DateTimeField()
    status=models.CharField(max_length=30)







