from django.urls import path, include
from albums import views


urlpatterns = [
    path('add/', views.AlbumAddView.as_view(), name='album-add'),
    path('<int:id>/', include([
        path('details/', views.AlbumDetailsView.as_view(), name='album-details'),
        path('edit/', views.AlbumEditView.as_view(), name='album-edit'),
        path('delete/', views.AlbumDeleteView.as_view(), name='album-delete'),
    ]))
]