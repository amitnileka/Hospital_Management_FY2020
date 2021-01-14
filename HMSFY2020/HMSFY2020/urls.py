"""HMSFY2020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Man_Hosp.views import *
from Man_Hosp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('about/', about,name="AboutUs"),
    path('login/', views.loginpage,name="login"),
    path('createAcc/', createAcc,name="createAcc"),
    path('contactus/',contactus,name="contactus"),
    path('services/',services,name="services"),
    path('patientinfo/',patientinfo,name="patientinfo"),
    path('logoutpg/',logoutpg,name='logoutpg'),
    path('patientprofile/',patientprofile,name="patientprofile"),

]
