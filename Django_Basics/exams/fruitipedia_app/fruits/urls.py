from django.urls import path, include
from fruits import views


urlpatterns = [
    path('create/', views.fruit_add_page, name='fruit-add'),
    path('<int:fruit_id>', include([
        path('details/', views.fruit_details_page, name='fruit-details'),
        path('edit/', views.fruit_edit_page, name='fruit-edit'),
        path('delete/', views.fruit_delete_page, name='fruit-delete'),
    ])),
]