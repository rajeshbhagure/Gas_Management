from django.shortcuts import render

# Create your views here.




from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from .models import CustomerModel, PriceModel
from .forms import CustomerForm, StockForm, PriceForm


class LoginClass(View):
    def get(self,request):
        return render(request, "agency/a_login.html")
    def post(self,request):
        user=request.POST['username']
        password=request.POST['password']
        if user=='rajesh' and password=='1234':
            request.session['user_id']=user
            return redirect('checklogin')
        else:
            messages.success(request,"Invalid Username And password")
            return redirect('a_login')


def checklogin(request):
    res=request.session.get('user_id',None)
    if res:
        return render(request, "agency/homepage.html")
    else:
        return redirect('a_login')


class Add_Cust(View):
    def get(self,request):
        return render(request,"agency/add_cust.html")
    def post(self,request):
        pass


class Add_Stock(View):

    def get(self,request):
        return render(request, "agency/add_stock.html", {"form": StockForm()})

    def post(self,request):
        if request.method=='POST':
            sf=StockForm(request.POST)
            if sf.is_valid():
                sf.save()
                messages.success(request,"The Stock Is Saved")
                return redirect('add_stock')


def logout(request):
    del request.session['user_id']
    return redirect('checklogin')


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


class CreateCust(View):
    def get(self,request):
        return render(request,"agency/create_cust.html",{"form":CustomerForm()})

    def post(self,request):
        if request.method=='POST':
            cf=CustomerForm(request.POST)
            if cf.is_valid():
                cf.save()
                messages.success(request,"The Customer Is Saved")
                return redirect('create_cust')


class ViewCust(View):
    def get(self,request):
        res=CustomerModel.objects.all()
        return render(request,"agency/viewall.html",{"data":res})
    def post(self,request):
        pass


class ViewUpdate(View):
    def get(self,request):
        res = CustomerModel.objects.all()
        return render(request, "agency/view_update.html", {"data": res})
    def post(self,request):
        pass


class Update(View):
    def get(self,request):
        id=request.GET.get('id')
        res=CustomerModel.objects.get(cust_no=id)
        return render(request, "agency/update.html", {"data": res})
    def post(self,request):
        pass


class ViewDelete(View):
    def get(self,request):
        res = CustomerModel.objects.all()
        return render(request, "agency/view_delete.html", {"data": res})

    def post(self,request):
        pass



def delete(request):
    id=request.GET.get('id')
    res=CustomerModel.objects.filter(cust_no=id)
    print(res)
    res.delete()
    messages.success(request,"Customer Data Is Deleted..")
    return redirect('view_delete')


class Price(View):
    def get(self,request):
        return render(request,"agency/Price.html")
    def post(self,request):
        pass


class Add_Price(View):
    def get(self,request):
        return render(request,"agency/add_price.html",{'form':PriceForm()})
    def post(self,request):
        if request.method=='POST':
            pf=PriceForm(request.POST)
            if pf.is_valid():
                pf.save()
                messages.success(request,"The Price Is Saved...")
                return redirect('add_price')


class ViewPrice(View):
    def get(self,request):
        res=PriceModel.objects.all()
        return render(request,"agency/view_price.html",{"data":res})
    def post(self,request):
        pass


class UpdatePrice(View):
    def get(self,request):
        res = PriceModel.objects.all()
        return render(request,"agency/update_price.html", {"data": res})

    def post(self,reqeust):
        pass

