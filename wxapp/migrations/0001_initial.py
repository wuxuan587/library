# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('name', models.CharField(default=b'wuxuan', max_length=20, serialize=False, primary_key=True)),
                ('department', models.TextField(max_length=20)),
                ('order_date', models.DateField(default=b'2018-01-01')),
                ('start_time', models.TimeField(default=b'09:00:00')),
                ('end_time', models.TimeField(default=b'10:00:00')),
                ('meeting_content', models.TextField(max_length=100)),
            ],
        ),
    ]
