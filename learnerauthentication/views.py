from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, "Incorrect username OR password")
            return redirect('login')
    else:
        return render(request, 'login.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, "signup.html")


@login_required(login_url="login")
def home(request):
    return render(request, "home.html")


def logoutuser(request):
    logout(request)
    return redirect("login")

def test(request):
    return render(request, "alt_home.html")

@login_required(login_url="login")
def new_parcel(request):
    return render(request, "new_parcel.html")