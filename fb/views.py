from django.shortcuts import render,redirect
from django.http import HttpResponse 
# Create your views here.
def login(request):
    return render(request,'login.html')

from .forms import UserForm

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://www.facebook.com')

    else:
        form = UserForm()
    
    return render(request, 'login.html', {'form': form})

def success(request):
    return render(request, 'success.html')