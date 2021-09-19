from django.urls import path
from roofsensors import views

urlpatterns = [
    path('data/', views.SensorDateview.as_view()),
]
