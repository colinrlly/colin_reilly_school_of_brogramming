from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chad/', views.chad, name='chad')
]
