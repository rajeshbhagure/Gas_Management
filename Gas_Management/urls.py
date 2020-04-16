"""Gas_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',TemplateView.as_view(template_name='index2.html'),name='index'),
    path('a_login/',views.LoginClass.as_view(),name='a_login'),
    path('checklogin/',views.checklogin,name='checklogin'),
    path('add_cust/',views.Add_Cust.as_view(),name='add_cust'),
    # path('add_price/',views.Add_Price.as_view(),name='add_price'),
    path('add_stock/',views.Add_Stock.as_view(),name='add_stock'),
    path('logout/',views.logout,name='logout'),
    path('c_login/',views.Cust_Login.as_view(),name='c_login'),
    path('cust_login',views.cust_login,name='cust_login'),
    path('cust_logout/',views.cust_logout,name='cust_logout'),
    path('update_cust/',views.UpdateCust.as_view(),name='update_cust'),
    path('create_cust/',views.CreateCust.as_view(),name='create_cust'),
    path('view_cust/',views.ViewCust.as_view(),name='view_cust'),
    path('view_update/',views.ViewUpdate.as_view(),name='view_update'),
    path('update/',views.Update.as_view(),name='update'),
    path('view_delete/',views.ViewDelete.as_view(),name='view_delete'),
    path('delete/',views.delete,name='delete'),
    path('price/',views.Price.as_view(),name='price')






]
