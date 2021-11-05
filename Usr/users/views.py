from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import UserForm, NameForm, ContactUs, UserUpdateForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
            return redirect('Usr-home')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})



def home(request):
    return render(request, 'users/home.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance, populate it with data from the request:
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'profile.html', {'form': form})

# @login_required
# def show_name(request):
#     return render(request, 'users/profile.html')


def contact(request):
    if request.method == 'POST':
        form = ContactUs(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            massage = form.cleaned_data.get('massage')

            subject = "someone contact us"
            content = f"""
            {first_name}{last_name} is trying contact to you. their email adrees is {email}. masage : {massage}"""
            send_mail(subject=subject, message=content, from_email='test.basic90@gmail.com', recipient_list=['test.basic90@gmail.com'])
            return redirect('thank_you')
    else:
        form = ContactUs()
    return render(request, 'users/contact_us.html', {'form': form})


def thank_you(request):
    return render(request, 'users/thank_you.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        form = UserUpdateForm

        return render(request, 'users/profile.html', {'form': form})