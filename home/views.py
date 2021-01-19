from django.shortcuts import render

from .forms import SearchForm


def home(request):
    """ Cette méthode sert à utiliser le formulaire pour la page home.html """
    form = SearchForm()
    return render(request, 'home.html', {
        "form":form
    })