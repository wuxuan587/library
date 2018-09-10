# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0004_auto_20180519_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='department',
            field=models.TextField(default=b'netcenter', max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='end_time',
            field=models.TimeField(default=b'10:00:00', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=b'2018-01-01', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_time',
            field=models.TimeField(default=b'09:00:00', null=True, blank=True),
        ),
    ]
