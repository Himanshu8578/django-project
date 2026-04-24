from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Home Page
def home(request):
    return render(request, 'home.html')


# Signup Page
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'signup.html')


# Login Page
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')


# Logout
def logout_view(request):
    logout(request)
    return redirect('login')


# Dashboard
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'dashboard.html')


# Edit Page (optional)
def edit(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'edit.html')
import openai
from django.conf import settings

def ai_response(request):
    if request.method == "POST":
        user_input = request.POST.get('prompt')

        openai.api_key = "YOUR_API_KEY"

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_input}]
        )

        reply = response['choices'][0]['message']['content']

        return render(request, "ai.html", {"response": reply})

    return render(request, "ai.html")
from django.shortcuts import render
import requests

def ai_page(request):
    response_text = ""

    if request.method == "POST":
        user_input = request.POST.get("prompt")
# 🤖 AI page
def ai_page(request):
    response_text = ""

    if request.method == "POST":
        user_input = request.POST.get("prompt")
        response_text = f"You asked: {user_input} 😄"

    return render(request, "ai.html", {"response": response_text})