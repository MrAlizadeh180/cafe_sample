from django.shortcuts import render
from django.views import generic
from .models import Table


# Create your views here.


class TableDetail(generic.DetailView):
    model = Table
    template_name = 'tables/table_orders.html'
