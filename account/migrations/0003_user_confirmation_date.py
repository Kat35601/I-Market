# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 16:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20171118_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirmation_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 16, 16, 18, 738276, tzinfo=utc)),
            preserve_default=False,
        ),
    ]