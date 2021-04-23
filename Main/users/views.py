from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    
    return render(request, 'users/single_user.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('users:index')
        else:
            return render(request, 'users/login.html', {'messege' : 'Invalid User'})

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {'messege' : 'Logged out.'})
