from django.shortcuts import render

# Create your views here.


from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

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

