import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# ---------------- HOME ----------------
def home(request):
    return render(request, 'home.html')


# ---------------- SIGNUP ----------------
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


# ---------------- LOGIN ----------------
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


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect('login')


# ---------------- DASHBOARD ----------------
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'dashboard.html')


# ---------------- EDIT PAGE ----------------
def edit(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'edit.html')


# ---------------- 🤖 AI PAGE (GEMINI FREE) ----------------
import requests
from django.shortcuts import render

def ai_page(request):
    response_text = ""

    if request.method == "POST":
        user_input = request.POST.get("prompt")

        try:
            response = requests.post(
                "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyARS8vcrhuIru165GPQatYpXtWR3tgCIMo",
                json={
                    "contents": [
                        {
                            "parts": [
                                {"text": user_input}
                            ]
                        }
                    ]
                }
            )

            data = response.json()
            print(data)   # debug ke liye

            if "candidates" in data:
                response_text = data['candidates'][0]['content']['parts'][0]['text']
            elif "error" in data:
                response_text = f"API Error: {data['error']}"
            else:
                response_text = str(data)

        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render(request, "ai.html", {"response": response_text})