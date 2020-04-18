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
from Consumer import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('c_login/',views.Cust_Login.as_view(),name='c_login'),
    path('cust_login',views.cust_login,name='cust_login'),
    path('cust_logout/',views.cust_logout, name='cust_logout'),
    path('account/',views.account, name='account'),
    path('update_cust/', views.UpdateCust.as_view(), name='update_cust'),

]
