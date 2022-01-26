from django.shortcuts import render
from django.views import generic
# Create your views here.
from .models import Order, OrderItem
from tables.models import Table


class CrateOrder(generic.edit.CreateView):
    model = Order
    fields = ['table']

    # def get(self, request, *args, **kwargs):
    #     kwargs.update({'item': 'lkjlk'})
    #     print(kwargs)
    #     return super().get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     table = Table.objects.get(id=int(request.POST.get('table')))
        # order = Order.objects.last()
        # asd = OrderItem(order=request.POST)
        # return super().post(request, *args, **kwargs)
        # asd.save()


class OrderDetail(generic.DetailView):
    model = Order
    template_name = 'orders/order_detail.html'


class OrderICreate(generic.CreateView):
    model = OrderItem
    fields = ['item', 'quantity', "order"]
    template_name = 'orders/asd.html'
    success_url = "/menu/categories"

    # def post(self, request, *args, **kwargs):
    #     order = Order.objects.get(id=1)
    #     kwargs.update({'order': order})
    #     return super().post(request, *args, **kwargs)
