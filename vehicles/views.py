from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, View
from django.contrib import messages

from .forms import (
    VehicleCreationForm,
    VehicleChangeForm,
    VehicleImageChangeForm,
)
from .models import Vehicle


class VehicleListView(LoginRequiredMixin, ListView):
    """View responsible of displaying all the vehicles of the currently logged
    user."""

    template_name = 'vehicles/list.html'

    def get_queryset(self):
        """Recovers all the vehicles owned by the current user."""
        return Vehicle.objects.filter(owner=self.request.user)


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    """View responsible of updating existing vehicles."""

    template_name = 'vehicles/edit.html'
    model = Vehicle
    form_class = VehicleChangeForm
    success_url = reverse_lazy('vehicles:list')


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    """View responsible of deleting a vehicle. It will display a confirmation
    page."""

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


class ImageChangeView(LoginRequiredMixin, View):
    """View responsible of handling the upload of a new image for the selected
    vehicle."""

    template_name = 'vehicles/image_change.html'
    form_class = VehicleImageChangeForm

    def get(self, request, pk, *args, **kwargs):
        """Answers to get HTTP requests: displays the form."""
        form = self.form_class()
        min_width, min_height = settings.VEHICLE_IMAGE_SIZE
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'vehicle_image_min_width': min_width,
                'vehicle_image_min_height': min_height,
            },
        )

    def post(self, request, pk, *args, **kwargs):
        """Answers to post HTTP requests: validates form and save data."""
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save(pk)
            return redirect('vehicles:edit', pk=pk)

        min_width, min_height = settings.VEHICLE_IMAGE_SIZE
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'vehicle_image_min_width': min_width,
                'vehicle_image_min_height': min_height,
            },
        )
