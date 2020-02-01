"""
    MyDjangoProject URL Configuration

    The `urlpatterns` list routes URLs to views. For more information please see:
        https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from django.urls import path
from MainApp import views as mainView
from FormApp import views as fView
from AuthApp import views as AView
from ApiApp.models import UserResource,AccessRecordResource

userRes = UserResource()
accessRecRes = AccessRecordResource()

urlpatterns = [
    path('',mainView.index,name='index'),
    path('admin/', admin.site.urls),
    path('MainApp/', include('MainApp.urls')),
    path('AuthApp/',include('AuthApp.urls')),
    path('form/',fView.form,name='form'),
    path('api/',include(userRes.urls)),
    path('api/',include(accessRecRes.urls)),
]
