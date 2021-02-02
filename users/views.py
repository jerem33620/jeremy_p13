from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth
from django.conf import settings

from vehicles.models import Vehicle

from .forms import SignupForm, AvatarChangeForm


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
    if request.method == 'POST':
        form = AvatarChangeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            return redirect('accountlog')
    else:
        form = AvatarChangeForm()
    min_width, min_height = settings.USER_AVATAR_SIZE
    return render(
        request,
        'avatar_change.html',
        {
            'form': form,
            'avatar_image_min_width': min_width,
            'avatar_image_min_height': min_height,
        },
    )
