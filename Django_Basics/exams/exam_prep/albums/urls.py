from django.urls import path, include
from albums import views


urlpatterns = [
    path('add/', views.add_album, name='album-add'),
    path('<int:id>/', include([
        path('details/', views.show_details_album, name='album-details'),
        path('edit/', views.edit_album, name='album-edit'),
        path('delete/', views.delete_album, name='album-delete'),
    ]))
]