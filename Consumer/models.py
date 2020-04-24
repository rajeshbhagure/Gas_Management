from django.db import models

# Create your models here.


class TransactionModel(models.Model):
    Tid=models.AutoField(primary_key=True)
    customer_id=models.IntegerField()
    cy_type=models.CharField(max_length=10)
    cust_name=models.CharField(max_length=30)
    datetime=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
