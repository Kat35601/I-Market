# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-19 22:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0009_auto_20171114_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(max_length=20, verbose_name='Postal code')),
                ('mobile', models.CharField(blank=True, max_length=12, null=True)),
                ('paid', models.BooleanField(default=False, verbose_name='Is paid')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Prices')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantities')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items', to='order.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Books', to='shop.Book')),
            ],
        ),
    ]
