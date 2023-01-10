from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.views import View
from core.models import User
from core.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

class SignupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'signup.html')
     
    def post(self, request, *args, **kwargs):
        # username, email, password, confirm_pass = signup_data(request)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_pass = request.POST['confirm_password']
        if username !='':
            if email !='':
                if password !='':
                    if confirm_pass !='':
                        if password == confirm_pass:
                            user = User.objects.create(username=username, email=email, password=password)
                            user.save()
                            return redirect('login')
                        else:
                            messages.error(request, "Password and Confirm Password  are not same.")
                    else:
                        messages.error(request, "Please Enter Confirm Password...")
                else:
                    messages.error(request, "Please Enter Password...")
            else:
                messages.error(request, "Please Enter Email...")
        else:
            messages.error(request, "Please Enter Username...")
        return redirect('signup')

class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('invite_team')
        """if request.GET['password']:
            password = request.GET['password']
            if password=='':
                print("-->Password: ",password)
            else:
                return redirect('home')
        return render(request, 'signin.html')"""
        try:
            password = request.GET['password']

            if password=='':
                print("-->Password: ",password)
                return render(request, 'create_password.html')
        except:
            return render(request, 'signin.html')



    def post(self, request, *args, **kwargs):   

        username = request.POST['user_name']
        password = request.POST['pass_word']

        print("username: ",username)
        print("password: ",password)

        # user = authenticate(username=username, password=password)
        userrrr = User.objects.get(username=username, password=password)
        print("user: ",userrrr)

        # if user is not None:    
        print("<<-->>")
        login(request, userrrr)
        print("-->>.Login Done")
        return redirect('invite_team')
        # else:
        #     return render(request, 'signin.html', {'errors':'Invalide Login Credential.'})

def send_invite_mail(user_mail, user):
    link = f'http://127.0.0.1:8000/login/?password={user.password}&id={user.id}'
    gmail_user = settings.EMAIL_HOST_USER
    to = [user_mail]
    subject = 'Email Verification'
    body = f"For joining the team Click the link: {link}"
    send_mail(subject=subject, from_email = gmail_user , message=body ,recipient_list =to, fail_silently=False)

class InviteTeamView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # return redirect('home')
            return render(request, 'invite.html')
        return render(request, 'invite.html')
        

    def post(self, request, *args, **kwargs):
        f_name = request.POST['Fname']
        l_name = request.POST['Lname']
        email = request.POST['Email']
        role = request.POST['bordered-radio']

        username = f_name+'_'+l_name

        user = User.objects.create(first_name=f_name, last_name=l_name, email=email, role=role, username=username)
        user.save()
        # print("__->:id: ",user.id)
        if user is not None:
            send_invite_mail(email, user)
            return redirect('invite_team')
        else:
            messages.error(request, 'Invite not sent...') 
            return redirect("invite_team")
        

