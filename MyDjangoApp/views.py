from django.shortcuts import render
from django.http import HttpResponse
from MyDjangoApp import views
from MyDjangoApp.userForm import UserForm 
from MyDjangoApp.models import Topic, Webpage, AccessRecord, User


def index(request):
    myDict={}
    return render(request,'index.html',context=myDict)

def welcome(request):
    myDict={}
    return render(request,'MyDjangoApp/welcome.html',context=myDict)
    
def accessRecords(request):

    webpgList = AccessRecord.objects.order_by('date')
    myDict = {'accessRecords': webpgList}

    return render(request,'MyDjangoApp/accessRecords.html',context=myDict)


def users(request):
    myUserForm = UserForm()

    userList = User.objects.order_by('fname')
    userDict = {'users': userList, 'userForm':myUserForm}

    return render(request,'MyDjangoApp/users.html',context=userDict )

def addUser(request):

    myUserForm = UserForm()

    userList = User.objects.order_by('fname')
    userDict = {'users': userList, 'userForm':myUserForm}


    if(request.method == 'POST'):
        form = UserForm(request.POST)

        if(form.is_valid()):
            form.save(commit=True)
            return users(request)
        else:
            print('Invalid user form!')
    return render(request,'MyDjangoApp/addUser.html',context=userDict )
