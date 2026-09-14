from django.urls import path
from .views import home
from api.api.api import product_api_view

urlpatterns = [
    path('', home, name='home'),
    path('product/', product_api_view, name='product_api'),
    path('product/<int:pk>/', product_api_view, name='product_api_detail'),
]