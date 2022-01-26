from django.urls import path
from .views import *
urlpatterns = [
    path('order_detail/<int:pk>', OrderDetail.as_view(), name='order_detail'),
    path('order_create/', CrateOrder.as_view(), name="create_order"),
    path('create_order_items/', OrderICreate.as_view(), name="create_order_item")
]