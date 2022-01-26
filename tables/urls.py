from django.urls import path
from .views import *

urlpatterns = [
    path('table_detail/<int:pk>', TableDetail.as_view(), name="table_detail"),
    path('table_money/<int:pk>', TableMoney.as_view(), name='table_money')
]
