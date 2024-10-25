from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView
from fruitipedia_app.utils import get_profile_obj
from fruits.models import Fruit
from profiles.forms import ProfileCreateForm


class IndexPageView(ListView, BaseFormView):
    model = Fruit
    form_class = ProfileCreateForm
    success_url = reverse_lazy('index-page')

    def get_template_names(self):
        profile = get_profile_obj()

        if profile:
            return ['common/dashboard.html']

        return ['common/index.html']


class DashboardView(ListView):
    model = Fruit
    template_name = 'common/dashboard.html'
