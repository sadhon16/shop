from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('ad/', views.OrderM, name='Ad'),
]