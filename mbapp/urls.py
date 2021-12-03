from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<str:product_id>', views.single_product, name='single_product'),
]