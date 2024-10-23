from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView
from albums.models import Album
from exam_prep.utils import get_profile_obj
from profiles.forms import ProfileCreateForm


class HomePageView(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        profile = get_profile_obj()

        if profile:
            return ['profiles/home-with-profile.html']

        return ['profiles/home-no-profile.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
