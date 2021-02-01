from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse

from bridges.models import Bridge
from vehicles.models import Vehicle

from .forms import SignupForm, AvatarChangeForm
from .models import User


def signup(request):
    """ Cette méthode sert à s'enregistrer """
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth.login(request, user)
            return redirect('pages:home')
    else:
        signup_form = SignupForm()
    return render(request, 'signup.html', {'signup_form': signup_form})


@login_required
def accountlog(request):
    """ Cette méthode sert à afficher le compte de l'utilisateur """
    vehicles = Vehicle.objects.filter(creator=request.user)
    return render(
        request,
        "account.html",
        {
            "account": request.user,
            "vehicles": vehicles,
        },
    )


@login_required
def avatar_change(request):
    user = request.user
    if request.method == 'POST':
        form = AvatarChangeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            return redirect('accountlog')
    else:
        form = AvatarChangeForm()
    return render(request, 'avatar_change.html', {'form': form})
