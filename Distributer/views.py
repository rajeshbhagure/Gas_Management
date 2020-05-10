from django.shortcuts import render

# Create your views here.




from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from Consumer.models import TransactionModel
from .models import CustomerModel, PriceModel
from .forms import CustomerForm, StockForm, PriceForm

from .models import Stockdetails


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


def logout(request):
    del request.session['user_id']
    return redirect('checklogin')

class Add_Cust(View):
    def get(self,request):
        return render(request,"agency/add_cust.html")
    def post(self,request):
        pass


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
        if request.method=='POST':
            cust_no=request.POST['cust_no']
            name=request.POST['name']
            contact=request.POST['contact']
            pincode=request.POST['pincode']
            address=request.POST['address']
            city=request.POST['city']
            Cy_type=request.POST['Cy_type']
            password=request.POST['password']
            CustomerModel.objects.filter(cust_no=cust_no).update(name=name,contact=contact,pincode=pincode,address=address,city=city,Cy_type=Cy_type,password=password)
            messages.success(request, "The Customer data is updated...")
            return redirect('view_update')


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
        res = PriceModel.objects.all()
        print(res)
        return render(request,"agency/view_price.html",{"data":res})
    def post(self,request):
        pass


class UpdatePrice(View):
    def get(self,request):
        res = PriceModel.objects.all()
        return render(request,"agency/update_price.html", {"data": res})

    def post(self,reqeust):
        pass


class UpdatedPrice(View):
    def get(self,request):
        id=request.GET.get('id')
        res=PriceModel.objects.get(p_id=id)
        return render(request,"agency/p_update.html",{"data":res})
    def post(self,request):
        pid=request.POST['p_id']
        print(pid)
        date=request.POST['date']
        ctype=request.POST['c_type']
        price=request.POST['price']
        PriceModel.objects.filter(p_id=pid).update(price=price)
        messages.success(request,"The price is updated...")
        return redirect('update_price')




class DeletePrice(View):
    def get(self,request):
        res=PriceModel.objects.all()
        return render(request,"agency/delete_price.html",{"data":res})
    def post(self,request):
        pass

def deleted_price(request):
    res = request.GET.get('id')
    PriceModel.objects.filter(p_id=res).delete()
    messages.success(request, "The Price Is deleted...")
    return redirect('delete_price')


def stock(request):
    return render(request,"agency/stock.html")



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


class View_Stock(View):
    def get(self,request):
        res=Stockdetails.objects.all()
        return render(request,"agency/View_stock.html",{'data':res})
    def post(self,request):
        pass


class UpdateViewStock(View):
    def get(self,request):
        res=Stockdetails.objects.all()
        return render(request,"agency/stock_update_view.html",{'data':res})
    def post(self,request):
        pass


class DeleteViewStock(View):
    def get(self,request):
        res = Stockdetails.objects.all()
        return render(request, "agency/stock_delete_view.html", {'data': res})
    def post(self,request):
        pass


def delete_stock(request):
    s_date=request.GET.get('id')
    Stockdetails.objects.filter(s_date=s_date).delete()
    return redirect('delete_view_stock')


def agency_booking(request):
    return render(request,"agency/Agency_Booking.html")


def pending(request):
    res=TransactionModel.objects.all().filter(status='Booking')
    return render(request,"agency/pending.html",{"data":res})


def processing(request):
    res=request.GET.get('id')
    print(res)
    TransactionModel.objects.filter(Tid=res).update(status='Pending')
    return redirect('pending')



def delivered(request):
    res = request.GET.get('id')
    TransactionModel.objects.filter(Tid=res).update(status='Delivered')
    return redirect('pending')


def book_pending(request):
    res = TransactionModel.objects.all().filter(status='Pending')
    return render(request, "agency/book_pending.html", {"data": res})


def booking_delivered(request):
    res = request.GET.get('id')
    TransactionModel.objects.filter(Tid=res).update(status='Delivered')
    return redirect('book_pending')


def book_delivered(request):
    res = TransactionModel.objects.all().filter(status='Delivered')
    return render(request, "agency/book_delivered.html", {"data": res})

