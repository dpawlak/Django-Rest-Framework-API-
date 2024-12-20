from django.urls import path
from rest_api import views

urlpatterns = [
    path('datapoints/', views.datapoint_list),
    path('datapoints/<int:pk>/', views.datapoint_detail),
]