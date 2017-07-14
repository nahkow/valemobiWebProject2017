from django.db import models
from django.core.urlresolvers import reverse

class Deal(models.Model):
    id = models.AutoField(primary_key=True)
    qtd = models.CharField(max_length=3)
    deal_item = models.ForeignKey('Item', on_delete=models.CASCADE)
    COMPRA = 'Compra'
    VENDA = 'Venda'
    DEAL_TYPE_CHOICES = (
        (VENDA , 'V'),
        (COMPRA , 'C'),

    )
    deal_type = models.CharField(
        max_length=6,
        choices=DEAL_TYPE_CHOICES,
        default=VENDA,
    )

    def get_absolute_url(self):
        return reverse('Market:index')
    def __str__(self):
        return 'Deal Type: ' + self.deal_type + ' | Item: ' \
               + self.deal_item.item_name + ' | Quantity: ' + str(self.qtd)


class Item(models.Model):
    item_code = models.AutoField(primary_key=True, max_length=20)
    item_name = models.CharField(max_length=500)
    item_price = models.DecimalField(max_digits=40, decimal_places=2)
    i_item_type = models.CharField(max_length=50, default='None')

    def get_absolute_url(self):
        return reverse('Market:index')

    def __str__(self):
        return ' | Name: ' \
               + self.item_name + ' | Type: ' + self.i_item_type + \
               ' | Price: ' + str(self.item_price)


        # class Item_type(models.Model):
        #     item_type_char = models.CharField(max_length=1, primary_key=True)
        #     item_type_ds = models.CharField(max_length=50)
        #
        #     def __str__(self):
        #         return self.item_type_char + ": " + self.item_type_ds
        #
        # class Deal_type(models.Model):
        #     deal_type_char = models.CharField(max_length=1, primary_key=True)
        #     deal_type_ds = models.CharField(max_length=50)
        #
        #     def __str__(self):
        #         return self.deal_type_char + ': ' + self.deal_type_ds
