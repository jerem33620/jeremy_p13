from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib import messages

from .forms import (
    VehicleCreationForm,
    VehicleChangeForm,
    VehicleImageChangeForm,
)
from .models import Vehicle


class VehicleListView(LoginRequiredMixin, ListView):
    template_name = 'vehicles/list.html'

    def get_queryset(self):
        return Vehicle.objects.filter(user=self.request.user)


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    """View responsible of updating existing vehicles."""

    template_name = 'vehicles/edit.html'
    model = Vehicle
    form_class = VehicleChangeForm
    success_url = reverse_lazy('vehicles:list')


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "vehicles/delete.html"
    model = Vehicle
    success_url = reverse_lazy('vehicles:list')


class VehicleCreateView(LoginRequiredMixin, CreateView):
    """View responsible of creating new vehicles."""

    template_name = 'vehicles/create.html'
    form_class = VehicleCreationForm
    success_url = reverse_lazy('vehicles:list')

    def get_context_data(self, **kwargs):
        """Customize data to be sent to the template."""
        context = super().get_context_data(**kwargs)
        min_width, min_height = settings.VEHICLE_IMAGE_SIZE
        context['vehicle_image_min_width'] = min_width
        context['vehicle_image_min_height'] = min_height
        return context

    def form_valid(self, form):
        """Sets the creator in the form vehicle instance."""
        form.instance.owner = self.request.user
        messages.add_message(
            self.request,
            messages.INFO,
            'Le nouveau véhicule a été enregistré !',
        )
        return super().form_valid(form)


@login_required
def image_change_view(request, pk):
    if request.method == 'POST':
        form = VehicleImageChangeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(pk)
            return redirect('vehicles:edit', pk=pk)
    else:
        form = VehicleImageChangeForm()

    min_width, min_height = settings.VEHICLE_IMAGE_SIZE
    return render(
        request,
        'vehicles/image_change.html',
        {
            'form': form,
            'vehicle_image_min_width': min_width,
            'vehicle_image_min_height': min_height,
        },
    )
