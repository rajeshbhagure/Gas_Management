# Generated by Django 3.0.1 on 2020-04-17 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('Tid', models.IntegerField()),
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cy_type', models.CharField(max_length=10)),
                ('cust_name', models.CharField(max_length=30)),
                ('datetime', models.DateTimeField()),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='PriceModel',
        ),
    ]
