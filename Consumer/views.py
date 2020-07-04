from django.shortcuts import render

# Create your views here.


from django.contrib import messages
from django.shortcuts import render, redirect

from datetime import date,datetime

# Create your views here.
from django.views.generic.base import View

from Consumer.forms import TransactionForm
from Consumer.models import TransactionModel
from Distributer.models import CustomerModel


class Cust_Login(View):
    def get(self,request):
        return render(request,"consumer/login.html")
    def post(self,request):
        uname=request.POST['username']
        password=request.POST['password']
        try:
            res=CustomerModel.objects.get(cust_no=uname,password=password)
            request.session['cust_id'] = res.name
            return redirect('cust_login')
        except CustomerModel.DoesNotExist:
            messages.error(request,"Invalid Username And Password")
            return redirect('c_login')

def cust_login(request):
    res=request.session.get('cust_id',None)
    if res:
        return render(request,"consumer/cust_home.html")
    else:
        return redirect('c_login')


def cust_logout(request):
    del request.session['cust_id']
    return redirect('cust_login')

def account(request):
    uname = request.GET.get('id')
    res = CustomerModel.objects.get(name=uname)
    print(res)
    return render(request, "consumer/account.html", {"data": res})


class UpdateCust(View):
    def get(self,request):
        uname=request.GET.get('id')
        res=CustomerModel.objects.filter(name=uname)
        print(res)
        return render(request,"consumer/update_cust.html",{"form":res})
    def post(self,request):
        no=request.POST['t1']
        password=request.POST['t2']
        name=request.POST['t3']
        address=request.POST['t4']
        city=request.POST['t5']
        contact=request.POST['t6']
        pincode=request.POST['t7']
        CustomerModel.objects.filter(cust_no=no).update(password=password,name=name,address=address,city=city,contact=contact,pincode=pincode)
        messages.success(request,"The Info Is Updated...")
        return redirect('update_cust')


class Booking(View):
    def get(self,request):
        id=request.GET.get('id')
        res=CustomerModel.objects.get(name=id)
        newdate=date.today()
        return render(request,"consumer/Booking.html",{'form':TransactionForm(),"data":res,'time':newdate})
    def post(self,request):
        if request.method=='POST':
            cust_no=request.POST.get('t1')
            print(cust_no)
            cy_type=request.POST.get('t2')
            cust_name=request.POST.get('t3')
            booking_date=datetime.now()
            booking_status=request.POST.get('t5')
            # contact=str(request.POST['t6'])
            # print(type(contact))
            # import requests
            # url = "https://www.fast2sms.com/dev/bulk"
            # payload = "sender_id=RBGAS&message= Hii This is Rajesh From Rb Gas Your Gas Cylinder Is Booked... &language=english&route=p&numbers=" + contact
            # headers = {
            #     'authorization': "fZYBQRum4eoMVFSp8jCGKcvNJX3hzLAak1ixO657d9IqHlTbDsNlbRn2drgWqC0mf469B35IuDyaOosZ",
            #     'Content-Type': "application/x-www-form-urlencoded",
            #     'Cache-Control': "no-cache",
            # }
            # response = requests.request("POST",url, data=payload, headers=headers)
            # response.json()
            # res=TransactionModel.objects.filter(cust_name=cust_name).latest(booking_date)
            # print(res)
            order=TransactionModel(customer_id=cust_no,cy_type=cy_type,cust_name=cust_name,datetime=booking_date,status=booking_status)
            order.save()
            messages.success(request, "Cylinder Is Boooked...")
            return render(request, "consumer/booked.html")


def history(request):
    id=request.GET.get('id')
    res=TransactionModel.objects.all().filter(cust_name=id)
    return render(request,"consumer/history.html",{"data":res})
