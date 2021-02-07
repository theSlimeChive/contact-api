from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact-list/', views.list),
    path('contact-detail/<str:pk>/', views.detail),
    path('contact-create/', views.create)
]