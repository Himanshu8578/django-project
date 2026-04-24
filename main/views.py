from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

# HOME
def home(request):
    return render(request, 'home.html')

# SIGNUP
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'User already exists'})

        user = User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'signup.html')

# LOGIN
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

# LOGOUT
def user_logout(request):
    logout(request)
    return redirect('login')

# DASHBOARD
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# VIRTUAL BG
@login_required
def virtual_bg(request):
    output_url = None

    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']

        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        input_path = fs.path(filename)

        output_filename = "output_" + filename
        output_path = os.path.join(settings.MEDIA_ROOT, output_filename)

        with open(input_path, 'rb') as i:
            with open(output_path, 'wb') as o:
                o.write(remove(i.read()))

        output_url = settings.MEDIA_URL + output_filename

    return render(request, 'virtual_bg.html', {'output_url': output_url})