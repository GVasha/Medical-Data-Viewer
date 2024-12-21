# viewer/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.table_view, name='table_view'),
    path('person_stats/', views.person_stats, name='person_stats'),
    path('product_stats/', views.product_stats, name='product_stats'),
    path('injection_stats/', views.injection_stats, name='injection_stats'),
]
