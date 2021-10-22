from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
            return redirect('Usr-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})



def home(request):
    return render(request, 'users/home.html')