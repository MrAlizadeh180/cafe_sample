from django.urls import path
from .views import *

urlpatterns = [
    path('MenuItems/', MenuItemsList.as_view(), name='menu_items_list')
]
