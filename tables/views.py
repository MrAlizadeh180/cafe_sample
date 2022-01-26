from django.shortcuts import render
from django.views import generic, View
from .models import Table


# Create your views here.


class TableDetail(generic.DetailView):
    model = Table
    template_name = 'tables/table_orders.html'


class TableMoney(View):
    def get(self, request, pk: int):
        context = {"money": None}
        return render(request, 'tables/table_money.html', context=context)

    def post(self, request, pk: int):
        date = request.POST.get('date')
        print("ghble error!!")
        table = Table.objects.get(id=pk)
        money = table.money
        print('money', money)
        context = {'money': money}
        return render(request, 'tables/table_money.html', context=context)
