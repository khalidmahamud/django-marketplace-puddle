import random
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView

from item.models import Category, Item
from .forms import SignUpForm, LoginForm

# Create your views here.


def index(request):
    items = Item.objects.filter(is_sold=False)
    sampled_items = random.sample(list(items), min(6, len(items)))
    categories = Category.objects.all()

    return render(
        request,
        "core/index.html",
        {"items": sampled_items, "categories": categories},
    )


def contact(request):
    return render(request, "core/contact.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("core:login")
    else:
        form = SignUpForm()

    return render(request, "core/signup.html", {"form": form})


class LoginView(LoginView):
    form_class = LoginForm
    template_name = "core/login.html"


def logout_user(request):
    logout(request)
    return redirect("core:index")
