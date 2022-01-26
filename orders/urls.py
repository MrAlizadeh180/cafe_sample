from django.urls import path
from .views import OrderDetail
urlpatterns = [
    path('order_detail/<int:pk>', OrderDetail.as_view(), name='order_detail')
]