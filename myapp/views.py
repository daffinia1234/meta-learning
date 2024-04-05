from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.forms import PersonForm, PropertyForm,SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here for menu.
def about(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    return render(request, "about.html", {'content': about_content})

def menu(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    return render(request, "menu.html", {'content': about_content})

def form_view(request):
    propertyObject=PropertyForm()
    if request.method=='POST':
        propertyObject=PropertyForm(request.POST)
        if propertyObject.is_valid():
            propertyObject.save()

    context={'form':propertyObject}

    return render(request,'property.html',context)


def hello_user(request):
    userForm=PersonForm()
    if request.method=='POST':
        userForm=PersonForm(request.POST)        
           
    context={'form':userForm, 'name': userForm['name'].value()}

    return render(request,'hello.html',context)

def user_sign_up(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()

            user=form.cleaned_data.get('username')
            messages.success(request,'account was created for ' + user)
            
            #User.objects.get()
            # create user profile and set 500 points for user profile
            return redirect('loginpage')
        
    context={'form':form}
    return render(request,'signup.html',context)

def user_login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('about')
        else:
            messages.info(request,"username or password is incorrect")

    context={}
    return render(request,'login.html',context)





