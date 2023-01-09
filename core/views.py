from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.views import View
from core.models import User
from core.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages

# Create your views here.
def signup_data(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm_pass = request.POST['confirm_password']

    print("--->> ",username)
    print("--->> ",email)
    print("--->> ",password)
    print("--->> ",confirm_pass)

    if username=="" and username==None:
        messages.error(request, "Username is required...")
    elif email=="" and email==None:
        messages.error(request, "Email is required...")
    elif password=="" and password==None:
        messages.error(request, "password is required...")
    elif confirm_pass=="" and confirm_pass==None:
        messages.error(request, "Confirm Password is required...")
    else:
        return username, email, password, confirm_pass 


class SignupView(View):
    def get(self, request, *args, **kwargs):
        # form = UserRegistrationForm()
        return render(request, 'signup.html')
     
    def post(self, request, *args, **kwargs):
        # print("--->",request.POST['username'])
        # username = request.POST['username']
        # email = request.POST['email']
        # email = request.POST['email']
        # email = request.POST['email']

        username, email, password, confirm_pass = signup_data(request)
        
        if password == confirm_pass:

        # form = UserRegistrationForm(request.POST , request.FILES)
        # if form.is_valid():
            
        #     profile_pic = form.cleaned_data['profile_pic']
        #     username = form.cleaned_data['username']
        #     email = form.cleaned_data['email']
        #     password = form.cleaned_data['password']

        #     # print("--->",request.POST['username'])

            user = User.objects.create(username=username, email=email, password=password)
            user.save()
            return redirect('login')
        else:
            messages.error(request, "Password and Confirm Password  are not same.")
            return redirect('signup')
        # form = UserRegistrationForm()

class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        form = UserLoginForm()
        return render(request, 'signin.html', {'form':form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        form = UserLoginForm()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('home')
        else:
            return redirect('login')
        
class InviteTeamView(View):
    pass
