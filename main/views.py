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

def dashboard(request):
    return render(request, 'dashboard.html')

def edit(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'edit.html')


# 🔥 AI FUNCTION (ONLY THIS ONE)
import requests
from django.shortcuts import render, redirect

def dashboard(request):
    return render(request, 'dashboard.html')

def edit(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'edit.html')


import requests

def ai_page(request):
    response_text = ""

    if request.method == "POST":
        user_input = request.POST.get("prompt")

        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": "Bearer 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",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://django-project-tuji.onrender.com",
                    "X-Title": "My Django AI App"
                },
                json={
                    "model": "openai/gpt-3.5-turbo",
                    "messages": [
                        {"role": "user", "content": user_input}
                    ]
                }
            )

            data = response.json()

            if "choices" in data:
                response_text = data["choices"][0]["message"]["content"]
            else:
                response_text = str(data)

        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render(request, "ai.html", {"response": response_text})