from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse

from home.forms import ConnexionForm, SearchForm, SignupForm
from .models import User


def login(request):
    """ Cette fonction sert à se connecter sur le site """
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(username=username, password=password)
            # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                auth.login(request, user)
                context = {
                    "user": request.user,
                }
                next = request.GET.get("next", "home")
                return redirect(next)
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()
    context = {"form":form}

    return render(request, 'login.html', context)

def logout(request):
    """ Cette méthode sert à se déconnecter """
    auth.logout(request)
    return redirect("home")

def signup(request):
    """ Cette méthode sert à s'enregistrer """
    form = SearchForm()
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth.login(request, user)
            return redirect('home')
    else:
        signup_form = SignupForm()
    return render(request, 'signup.html', {'signup_form': signup_form, 'form': form })

def accountlog(request):
    """ Cette méthode sert à afficher le compte de l'utilisateur """
    form = SearchForm()
    account = User(request)
    return render(request, "account.html", {
        "account": account, "form": form,
    })