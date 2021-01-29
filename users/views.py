from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse

from .forms import SignupForm
from .models import User
from bridges.models import Bridge
from vehicles.models import Vehicle


def signup(request):
    """ Cette méthode sert à s'enregistrer """
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth.login(request, user)
            return redirect('home')
    else:
        signup_form = SignupForm()
    return render(request, 'signup.html', {'signup_form': signup_form})


def accountlog(request):
    """ Cette méthode sert à afficher le compte de l'utilisateur """
    num_bridges = Bridge.objects.filter(creator=request.user).count()
    num_vehicles = Vehicle.objects.filter(creator=request.user).count()
    return render(
        request,
        "account.html",
        {
            "account": request.user,
            "num_bridges": num_bridges,
            "num_vehicles": num_vehicles,
        },
    )
