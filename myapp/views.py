from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Alumni, Post
from .forms import PostForm
from django.urls import reverse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django import forms
from django.shortcuts import render

def home(request):
    alumni_list = Alumni.objects.all()
    posts = Post.objects.all().order_by('-created_at')  # Fetch latest posts

    form = PostForm()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success(request, "Post created successfully!")
                return redirect("home")
            else:
                messages.error(request, "Error in post submission. Please check your inputs.")
        else:
            messages.warning(request, "You must be logged in to post.")
            return redirect("login")

    context = {
        "alumni_list": alumni_list,
        "posts": posts,
        "form": form
    }
    return render(request, "home.html", context)

@login_required
def profile(request, alumni_id=None):
    if alumni_id is None:
        return redirect(reverse("profile_with_id", kwargs={"alumni_id": request.user.id}))

    alumni = get_object_or_404(Alumni, id=alumni_id)
    return render(request, "profile.html", {"alumni": alumni})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return render(request, "login.html", {"error": "Invalid credentials."})

    return render(request, "login.html")

@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  # Encrypt password
            user.save()
            login(request, user)  # Auto-login after signup
            messages.success(request, "Account created successfully!")
            return redirect("home")
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})

def resume_matcher(request):
    return render(request, "resume_matcher.html")

def chatbot(request):
    return render(request, "chatbot.html")

def radar_plot(request):
    return render(request, "radar_plot.html")

def pdf_analyzer(request):
    return redirect("pdf_analyzer.html")
