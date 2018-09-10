# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='department',
            field=models.TextField(default=b'netcenter', max_length=20),
        ),
    ]
