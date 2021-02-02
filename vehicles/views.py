from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import VehicleCreationForm


class VehicleCreate(LoginRequiredMixin, CreateView):
    """View responsible of creating new vehicles."""

    template_name = 'vehicles/create.html'
    form_class = VehicleCreationForm
    success_url = reverse_lazy('vehicles:create')

    def get_context_data(self, **kwargs):
        """Customize data to be sent to the template."""
        context = super().get_context_data(**kwargs)
        min_width, min_height = settings.VEHICLE_IMAGE_SIZE
        context['vehicle_image_min_width'] = min_width
        context['vehicle_image_min_height'] = min_height
        return context

    def form_valid(self, form):
        """Sets the creator in the form vehicle instance."""
        form.instance.creator = self.request.user
        return super().form_valid(form)
