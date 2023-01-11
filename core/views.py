from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.views import View
from core.models import User
from core.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import uuid


# Create your views here.

class SignupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'signup.html')
     
    def post(self, request, *args, **kwargs):
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
                            messages.error(request, "Password and Confirm Password are not same.")
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
            return redirect('dashboard')
        try:
            user = User.objects.get(uuid=request.GET.get('uuid'))
            password = user.password
            # password = request.GET['password']
            if password=='':
                print("-->Password: ",password)
                return render(request, 'invited_user_set_password.html')
            return render(request, 'signin.html')
            
        except:
            return render(request, 'signin.html')

    def post(self, request, *args, **kwargs):
        
        password = request.GET.get('password')
        if password=='':
            id = request.GET['uuid']
            pass_word = request.POST['password-1']
            conf_pass = request.POST['confirmpassword-1']
            if pass_word==conf_pass:
                user = User.objects.get(uuid=id)
                user.password=pass_word
                user.save()
                if user is not None:
                    login(request, user)
                    return redirect("dashboard")
            else:
                return render(request, 'invited_user_set_password.html', {'errors':'Error: Password and Confirm Password  are not same...'})
        else:
            username = request.POST['user_name']
            password = request.POST['pass_word']
            if User.objects.filter(username=username, password=password).exists():   
                user = User.objects.get(username=username, password=password)
                print("user: ",user)
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'signin.html', {'errors':'Error: Invalide Login Credential.'})  


def send_invite_mail(user_mail, user):
    link = f'http://127.0.0.1:8000/login/?password={user.password}&uuid={user.uuid}'
    gmail_user = settings.EMAIL_HOST_USER
    to = [user_mail]
    subject = 'Email Verification'
    body = f"For joining the team Click the link: {link}"
    send_mail(subject=subject, from_email = gmail_user , message=body ,recipient_list =to, fail_silently=False)

class InviteTeamView(View):
    def get(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        #     user = request.user
        #     if user=="Admin":
                return render(request, 'invite.html')
            # else:
            #     return render(request, 'dashboard.html',{'error':'Error: You are not Admin...'})
        
    def post(self, request, *args, **kwargs):
        f_name = request.POST['Fname']
        l_name = request.POST['Lname']
        email = request.POST['Email']
        role = request.POST['bordered-radio']

        if f_name != '':
            if l_name != '':
                if email != '':
                    if role != '':
                        uu_id = str(uuid.uuid4().hex[:8])
                        username = f_name+'  '+l_name
                        user = User.objects.create(first_name=f_name, last_name=l_name, email=email, role=role, username=username, uuid=uu_id)
                        user.save()
                        if user is not None:
                            send_invite_mail(email, user)
                            return redirect('dashboard')
                        else:
                            messages.error(request, 'Invite not sent...')
                    else:
                        messages.error(request, "Please Select Role...")
                else:
                    messages.error(request, "Please Enter Email...")
            else:
                messages.error(request, "Please Enter Last-name...")
        else:
            messages.error(request, "Please Enter First-name...")
        return redirect('invite_team')
        
class DashboardView(View):
    def get(self,request):
        return render(request, 'dashboard.html')