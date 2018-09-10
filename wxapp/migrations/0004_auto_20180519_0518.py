# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0003_auto_20180519_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='department',
            field=models.TextField(default=b'netcenter', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='meeting_content',
            field=models.TextField(max_length=100),
        ),
    ]
