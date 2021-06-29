from django.urls import path
from .views import customer_list
from .views import customer_detail

urlpatterns = [
    path('', customer_list, name="customer-list"),
    path('customer/<str:slug>/', customer_detail, name="customer-detail")
]