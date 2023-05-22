from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
#def index(request):
#    return render(request, 'login/login.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                    login (request, user)
                    return redirect('dashboard')
            else:
                messages.info(request, 'Username hoặc password không đúng')

        context = {}
        return render(request, 'login/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')
