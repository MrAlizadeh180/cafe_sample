from django.urls import path
from .views import TableDetail

urlpatterns = [
    path('table_detail/<int:pk>', TableDetail.as_view(), name="table_detail")
]
