from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
# Create your views here.

#to display my main page that is user registration or login
def index(request):
    return render(request,"login/index.html")

#register route for creating a user/new user
def register(request):
    errors = User.objects.validator(request.POST,"registration")
    #print(errors) 
    if errors:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/') 
    else:
        User.objects.create(first_name = request.POST['register_fname'],
                        last_name = request.POST['register_lname'],
                        email = request.POST['register_email'],
                        password = request.POST['register_pwd'])
        thisUser = User.objects.last()
        request.session['user_id'] = thisUser.id
        request.session['user_fname'] = thisUser.first_name
        return redirect("/feedapp")  # check for bothcase redirecting properly or not /feedapp
        
def login(request):
    checkUser = User.objects.filter(email=request.POST['log-email'],password = request.POST['log-pwd'])
    if (len(checkUser) < 1):
        messages.error(request, "The email  password do not match in our databases")
        return redirect("/")
    else:
        request.session['user_id'] = checkUser[0].id
        request.session['user_fname'] = checkUser[0].first_name
        return redirect("/feedapp")