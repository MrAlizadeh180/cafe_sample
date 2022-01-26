from django.urls import path
from .views import *
urlpatterns = [
    path('order_detail/<int:pk>', OrderDetail.as_view(), name='order_detail'),
    path('order_create/', CrateOrder.as_view()),
    # path('or_it/', OrderICreate.as_view())
]