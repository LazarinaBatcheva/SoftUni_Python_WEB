from django.urls import path, include
from fruits import views


urlpatterns = [
    path('create/', views.FruitAddView.as_view(), name='fruit-add'),
    path('<int:fruit_id>', include([
        path('details/', views.FruitDetailsView.as_view(), name='fruit-details'),
        path('edit/', views.FruitEditView.as_view(), name='fruit-edit'),
        path('delete/', views.FruitDeleteView.as_view(), name='fruit-delete'),
    ])),
]