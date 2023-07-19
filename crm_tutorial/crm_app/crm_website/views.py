from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    # check to see if logging in
    if request.method == "POST":
        # get the username and password
        username = request.POST['username']
        password = request.POST['password']

        # authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # login the user
            login(request, user)
            # return a success message
            messages.success(request, "You have successfully logged in!")
            # redirect to home page
            return redirect("home")

        else:
            # return an error message
            messages.success(request, "Invalid username or password. Please try again.")
            # redirect to home page
            return redirect("home")

    else:
        return render(request, "home.html", {})


# def login_user(request):
#     pass

def logout_user(request):
    pass
