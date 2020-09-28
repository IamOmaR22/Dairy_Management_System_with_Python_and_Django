from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from dairyapp.forms import contactForm, SignUpForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    title = ''
    confirm_message = None
    form = contactForm(request.POST or None)
    if form.is_valid():
        receivers_list = ['omarfaruk2468@gmail.com']
        subject = form.cleaned_data['subject']
        name = form.cleaned_data['name']
        comment = form.cleaned_data['message']
        emailFrom = form.cleaned_data['email']
        message = f'Name: {name}\nEmail Id: {emailFrom}\nMessage: {comment}'
        emailsender = settings.EMAIL_HOST_USER
        send_mail(subject, message, emailsender, receivers_list, fail_silently=False)
        title ="Thanks!"+' '+name
        confirm_message = "Thanks for the message. We will get right back to you."
        form = None
    context = {'title': title, 'form':form, 'confirm_message': confirm_message}
    temp = 'home.html'
    return render(request, temp, context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # If you want to login user after signup, than use this code
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)

            # return redirect('addcustomer')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
