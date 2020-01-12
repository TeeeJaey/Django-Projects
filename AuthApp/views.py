from django.shortcuts import render
from AuthApp.forms import UserForm,UserProfileInfoForm


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def userSignUp(request):

    signedUp = False

    if(request.method == "POST"):
        userForm = UserForm(data=request.POST)
        profileForm = UserProfileInfoForm(data=request.POST)

        if(userForm.is_valid() and profileForm.is_valid()):
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            profile = profileForm.save(commit=False)
            profile.user = user


            if('profilePic' in request.FILES):
                profile.profilePic = request.FILES['profilePic']
            profile.save()

            signedUp = True
        else:
            print(userForm.errors, profileForm.errors)
    else:
        userForm = UserForm()
        profileForm = UserProfileInfoForm()

    return render(request, 'AuthApp/signUp.html', {'signedUp': signedUp,'userForm':userForm, 'profileForm':profileForm})


@login_required
def userSignOut(request):  
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def userSignIn(request):

    if(request.method == "POST"):
        username = request.POST.get('username')        
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if(user):
            if(user.is_active):
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active!")
        else:
            print("Sign In Falied!")
            print("Username: {} , Password: {}".format(username,password))
            return HttpResponse("Invalid login details!")
    
    else:
        return render(request, 'AuthApp/signIn.html', {})