from django.urls import path
from roofsensors import views

urlpatterns = [
    path('data/', views.SensorDataView.as_view()),
    path('data/ambient/', views.AmbientSensorDataView.as_view()),
]
