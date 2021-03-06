# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 06:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qtd', models.CharField(max_length=3)),
                ('deal_type', models.CharField(choices=[('Venda', 'V'), ('Compra', 'C')], default='Venda', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_code', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=500)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=40)),
                ('i_item_type', models.CharField(default='None', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='deal',
            name='deal_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Market.Item'),
        ),
    ]
