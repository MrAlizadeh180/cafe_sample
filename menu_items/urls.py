from django.urls import path
from .views import *

urlpatterns = [
    path('menu_items/', MenuItemsList.as_view(), name='menu_items_list'),
    path('categories/', CategoryList.as_view(), name="categories")
]
