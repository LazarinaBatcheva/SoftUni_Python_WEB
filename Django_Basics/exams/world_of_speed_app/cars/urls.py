from django.urls import path, include

from cars import views


urlpatterns = [
    path('catalogue/', views.catalogue_page, name='catalogue-page'),
    path('create/', views.add_car, name='car-add'),
    path('<int:id>/', include([
        path('details/', views.car_details_page, name='car-details'),
        path('edit/', views.edit_car, name='car-edit'),
        path('delete/', views.delete_car, name='car-delete'),
    ]))
]