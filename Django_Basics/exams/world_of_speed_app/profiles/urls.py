from django.urls import path
from profiles import views


urlpatterns = [
    path('create/', views.add_profile, name='profile-add'),
    path('details/', views.profile_details_page, name='profile-details'),
    path('edit/', views.edit_profile, name='profile-edit'),
    path('delete/', views.delete_profile, name='profile-delete'),
]