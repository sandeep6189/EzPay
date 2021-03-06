"""ezPayProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import ezPayApp.views

urlpatterns = [
    url(r'^home', ezPayApp.views.home,name="home"),
    url(r'^$', ezPayApp.views.loginpage),
    url(r'^login', ezPayApp.views.loginpage,name="loginpage"),
	url(r'^schlogin', ezPayApp.views.schLogin,name="schlogin"),
    url(r'^transfer', ezPayApp.views.transfer,name="transfer"),
    url(r'^shopping', ezPayApp.views.shopping,name="shopping")

]
