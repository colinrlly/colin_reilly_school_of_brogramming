from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cumbox/', views.cumbox, name='cumbox'),
]