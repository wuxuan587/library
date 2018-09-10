# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0005_auto_20180519_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='meeting_content',
            field=models.TextField(max_length=100, blank=True),
        ),
    ]
