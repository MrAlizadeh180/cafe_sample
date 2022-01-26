from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, MenuItem


# Create your views here.


class MenuItemsList(ListView):
    model = MenuItem
    template_name = 'menu_items/menu_item/sample.html'


class CategoryList(ListView):
    model = Category
    template_name = 'menu_items/category/sample.html'
