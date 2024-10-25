from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from fruitipedia_app.utils import get_profile_obj
from fruits.forms import FruitAddForm, FruitEditForm, FruitDeleteForm
from fruits.models import Fruit


class FruitAddView(CreateView):
    model = Fruit
    form_class = FruitAddForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = get_profile_obj()
        return super().form_valid(form)


class FruitEditView(UpdateView):
    model = Fruit
    form_class = FruitEditForm
    pk_url_kwarg = 'fruit_id'
    template_name = 'fruits/edit-fruit.html'
    success_url = reverse_lazy('dashboard')


class FruitDeleteView(DeleteView):
    model = Fruit
    form_class = FruitDeleteForm
    pk_url_kwarg = 'fruit_id'
    template_name = 'fruits/delete-fruit.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class FruitDetailsView(DetailView):
    model = Fruit
    pk_url_kwarg = 'fruit_id'
    template_name = 'fruits/details-fruit.html'
