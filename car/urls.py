from django.urls import path
from . import views

urlpatterns = [
    path('getcars', views.GetAllCars.as_view()),
]