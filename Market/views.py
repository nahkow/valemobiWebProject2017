from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Deal,Item
from django.views.generic import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy


def index(request):
    all_deals = Deal.objects.all()
    all_items= Item.objects.all()
    context = {
        'all_deals' : all_deals
        ,'all_items' : all_items
    }

    return render(request , 'Market/index.html' , context)

def item_details(request, item_c):
        return HttpResponse(
            '<h1>'
            'Details for Item: ' + str(item_c) +
            '</h1>'

        )

class CreateItem(CreateView):
    model = Item
    fields = ['item_name','item_price','i_item_type']

class CreateDeal(CreateView):
    model = Deal
    fields = ['deal_item', 'deal_type', 'qtd']

class DeleteDeal(DeleteView):
    model = Deal
    success_url = reverse_lazy('Market:index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# Not implemented Yet =(
#
# class DeleteItem(DeleteView):
#     model = Item
#     success_url = reverse_lazy('Market:index')
#
# class UpsateItem(UpdateView):
#     model = Item
#     fields = ['item_name','item_price','i_item_type']
#
# class UpdateDeal(UpdateView):
#     model = Deal
#     fields = ['deal_item', 'deal_type', 'qtd']