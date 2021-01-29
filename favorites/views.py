from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from home.forms import SearchForm
from bridges.models import Bridge
from favorites.models import Favorite
from vehicles.models import Vehicle


# @login_required()
# def favorite_save(request):
#     """Sert à sauvegarder les produits enregistrées par les utilisateurs"""
#     if request.method == "POST":
#         substitute_code = int(request.POST.get("substitute-code"))
#         product_code = int(request.POST.get("product-code"))
#         substitute = Product.objects.get(code=substitute_code)
#         product = Product.objects.get(code=product_code)

#         if substitute and product:
#             Favorite.objects.get_or_create(user=request.user, product=product, substitute=substitute)

#         return redirect("product_info", substitute_code)

#     return redirect("home")

@login_required()
def favorite_list(request):
    """Sert à afficher les produits sauvegarder par les utilisateurs"""
    form = SearchForm()
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, "account.html", {
        "favorites":favorites, "form": form,
    })
