from django.urls import path

from profiles import views

urlpatterns = [
    path('details/', views.show_profile_details, name='profile-details'),
    path('delete/', views.delete_profile, name='profile-delete'),
]