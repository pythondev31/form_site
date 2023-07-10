from django.urls import path
from .views import *
urlpatterns = [
    path('', customer_form, name="customer-form"),
    path('list/',customers_list, name="customers-list")
]