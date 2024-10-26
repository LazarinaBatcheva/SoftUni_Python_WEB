from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from cars.forms import CarAddForm, CarEditForm, CarDeleteForm
from cars.models import Car
from world_of_speed_app.utils import get_profile_obj


class CataloguePageView(ListView):
    model = Car
    template_name = 'cars/catalogue.html'


class CarAddView(CreateView):
    model = Car
    form_class = CarAddForm
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('catalogue-page')

    def form_valid(self, form):
        form.instance.owner = get_profile_obj()
        return super().form_valid(form)


class CarEditView(UpdateView):
    model = Car
    form_class = CarEditForm
    pk_url_kwarg = 'id'
    template_name = 'cars/car-edit.html'
    success_url = reverse_lazy('catalogue-page')


class CarDeleteView(DeleteView):
    model = Car
    form_class = CarDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('catalogue-page')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class CarDetailsView(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'cars/car-details.html'
