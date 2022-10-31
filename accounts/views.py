from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def login_view(request):
    form = AuthenticationForm(request, data=request.POST)
    print(dir(form))
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("/")
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    return render(request, 'accounts/logout.html')

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')

    context = {
        "form": form
    }
    return render(request, "accounts/register.html", context=context)