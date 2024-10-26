from django.urls import path, include

from cars import views


urlpatterns = [
    path('catalogue/', views.CataloguePageView.as_view(), name='catalogue-page'),
    path('create/', views.CarAddView.as_view(), name='car-add'),
    path('<int:id>/', include([
        path('details/', views.CarDetailsView.as_view(), name='car-details'),
        path('edit/', views.CarEditView.as_view(), name='car-edit'),
        path('delete/', views.CarDeleteView.as_view(), name='car-delete'),
    ]))
]