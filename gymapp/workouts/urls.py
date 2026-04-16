from django.urls import path
from . import views

urlpatterns = [
    path('',views.workout),
    path('/chest',views.chest),
    path('/back',views.back),
    path('/abs',views.abs),
    path('/shoulder',views.shoulder),
    path('/legs',views.legs),
    path('/comeback',views.comeback),
    
]
