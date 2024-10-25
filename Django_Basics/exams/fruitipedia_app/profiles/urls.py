from django.urls import path
from profiles import views


urlpatterns = [
    path('create/', views.profile_create_page, name='profile-create'),
    path('details/', views.profile_details_page, name='profile-details'),
    path('edit/', views.profile_edit_page, name='profile-edit'),
    path('delete/', views.profile_delete_page, name='profile-delete'),
]