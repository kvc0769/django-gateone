"""django_gateone URL Configuration

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
from django.contrib.auth.decorators import login_required
from applications.views import index,auth
from django.contrib.auth.views import login,logout
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',login_required(index.as_view())),
    url(r'^auth/$',auth.as_view()),
    url(r'^accounts/login/$', LoginView.as_view(template_name='admin/login.html'),),
    url(r'^accounts/logout/$',LogoutView.as_view(template_name='registration/logged_out.html'),),    
]
