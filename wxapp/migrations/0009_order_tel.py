# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0008_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tel',
            field=models.IntegerField(default=319, max_length=11),
        ),
    ]
