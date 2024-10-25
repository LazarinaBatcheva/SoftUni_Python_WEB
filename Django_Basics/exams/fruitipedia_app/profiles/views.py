from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from profiles.forms import ProfileCreateForm, ProfileEditForm
from profiles.mixins import ProfileObjectMixin
from profiles.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('dashboard')


class ProfileEditView(ProfileObjectMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('profile-details')


class ProfileDeleteView(ProfileObjectMixin, DeleteView):
    template_name = 'profiles/delete-profile.html'
    success_url = reverse_lazy('index-page')


class ProfileDetailsView(ProfileObjectMixin, DetailView):
    model = Profile
    template_name = 'profiles/details-profile.html'
