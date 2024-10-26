from django.urls import path
from common import views


urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index-page'),
]