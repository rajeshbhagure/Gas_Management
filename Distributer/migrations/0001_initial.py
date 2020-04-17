# Generated by Django 3.0.1 on 2020-04-17 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('cust_no', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('Cy_type', models.CharField(max_length=10)),
                ('date_conn', models.DateField()),
                ('name', models.CharField(max_length=30, unique=True)),
                ('address', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stockdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_date', models.DateTimeField()),
                ('stock_comm', models.IntegerField()),
                ('stock_dom', models.IntegerField()),
                ('defective_comm', models.IntegerField()),
                ('defective_dom', models.IntegerField()),
                ('current_stock_comm', models.IntegerField()),
                ('current_stock_dom', models.IntegerField()),
            ],
        ),
    ]
