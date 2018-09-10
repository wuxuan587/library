# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0007_auto_20180519_0522'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('name', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('tel', models.IntegerField(default=25, max_length=10)),
            ],
        ),
    ]
