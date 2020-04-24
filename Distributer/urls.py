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
from Distributer import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('a_login/',views.LoginClass.as_view(),name='a_login'),
    path('checklogin/',views.checklogin,name='checklogin'),
    path('logout/',views.logout,name='logout'),
    path('add_cust/',views.Add_Cust.as_view(),name='add_cust'),
    path('create_cust/',views.CreateCust.as_view(),name='create_cust'),
    path('view_cust/',views.ViewCust.as_view(),name='view_cust'),
    path('view_update/',views.ViewUpdate.as_view(),name='view_update'),
    path('update/',views.Update.as_view(),name='update'),
    path('view_delete/',views.ViewDelete.as_view(),name='view_delete'),
    path('delete/',views.delete,name='delete'),
    path('price/',views.Price.as_view(),name='price'),
    path('add_price/',views.Add_Price.as_view(),name='add_price'),
    path('view_price/',views.ViewPrice.as_view(),name='view_price'),
    path('update_price/',views.UpdatePrice.as_view(),name='update_price'),
    path('updated_price/',views.UpdatedPrice.as_view(),name='updated_price'),
    path('delete_price/',views.DeletePrice.as_view(),name='delete_price'),
    path('deleted_price/',views.deleted_price,name='deleted_price'),
    path('stock/',views.stock,name='stock'),
    path('add_stock/', views.Add_Stock.as_view(), name='add_stock'),
    path('view_stock/', views.View_Stock.as_view(), name='view_stock'),
    path('update_view_stock/',views.UpdateViewStock.as_view(),name='update_view_stock'),
    path('delete_view_stock/',views.DeleteViewStock.as_view(),name='delete_view_stock'),
    path('delete_stock/',views.delete_stock,name='delete_stock')

]
