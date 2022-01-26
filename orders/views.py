from django.shortcuts import render
from django.views import generic
# Create your views here.
from .models import Order


class CrateOrder(generic.edit.CreateView):
    model = Order
    fields = ['table']


class OrderDetail(generic.DetailView):
    model = Order
    template_name = 'orders/order_detail.html'

