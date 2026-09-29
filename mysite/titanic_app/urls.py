from django.urls import path,include
from .views import PredictAliveViewSet



urlpatterns=[
    path('predict_alive',PredictAliveViewSet.as_view(),name='predict-alive')
]