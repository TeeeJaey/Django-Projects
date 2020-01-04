from django.shortcuts import render
from .form import FormName
# Create your views here.


def index(request):

    return render(request, 'form.html')


def form(request):
    myform = FormName()

    if(request.method == 'POST'):
        myform = FormName(request.POST)

        if(myform.is_valid()):
            print("Name: " + myform.cleaned_data['name'])
            print("Email: " + myform.cleaned_data['email'])
            print("Text: " + myform.cleaned_data['text'])


    return render(request, 'form.html' , {'form':myform})

