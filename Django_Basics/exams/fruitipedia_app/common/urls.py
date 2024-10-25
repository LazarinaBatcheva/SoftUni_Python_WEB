from django.urls import path
from common import views


urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('dashboard/', views.dashboard_page, name='dashboard')
]