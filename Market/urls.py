from django.conf.urls import url
from django.contrib import admin
from . import views

import Market

app_name = 'Market'


urlpatterns = [
    # market/ or market/index/
    url(r'^$', views.index, name='index'),
    # market/item/54/
    url(r'^item/(?P<item_c>[0-9]+)/$', views.item_details, name='item_details'),

    # Create
    url(r'addItem/$', views.CreateItem.as_view(), name='create_item'),
    url(r'addDeal/$', views.CreateDeal.as_view(), name='create_Deal'),

    # Delete
    url(r'Deal/(?P<pk>[0-9]+)/delete/$', views.DeleteDeal.as_view(), name='delete_deal'),
#     url(r'deleteItem/(?P<pk>[0-9]+)/$', views.DeleteItem.as_view(), name='delete_item'),

]
