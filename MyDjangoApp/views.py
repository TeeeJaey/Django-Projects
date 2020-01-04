from django.shortcuts import render
from django.http import HttpResponse
from MyDjangoApp import views
from MyDjangoApp.userForm import UserForm 
from MyDjangoApp.models import Topic, Webpage, AccessRecord, User



def index(request):

    webpgList = AccessRecord.objects.order_by('date')
    dateDict = {'accessRecords': webpgList}

    return render(request,'MyDjangoApp/index.html',context=dateDict)


def users(request):

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
    return render(request,'MyDjangoApp/users.html',context=userDict )
