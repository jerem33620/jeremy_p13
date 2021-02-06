from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

from .forms import BridgeCreationForm


class BridgeCreate(View):
    def get(self, request, *args, **kwargs):
        form = BridgeCreationForm(request)
        return render(request, 'bridges/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = BridgeCreationForm(request, request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.INFO, 'Le nouveau pont a été enregistré !'
            )
            return redirect('bridges:create')
        return render(request, 'bridges/register.html', {'form': form})