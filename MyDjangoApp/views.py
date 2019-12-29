from django.shortcuts import render
from django.http import HttpResponse
from MyDjangoApp import views
from MyDjangoApp.models import Topic, Webpage, AccessRecord, User



def index(request):

    webpgList = AccessRecord.objects.order_by('date')
    dateDict = {'accessRecords': webpgList}

    return render(request,'MyDjangoApp/index.html',context=dateDict)


def users(request):

    userList = User.objects.order_by('fname')
    userDict = {'users': userList}

    return render(request,'MyDjangoApp/users.html',context=userDict)
