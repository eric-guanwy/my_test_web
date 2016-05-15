# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20160515_1308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={},
        ),
        migrations.RemoveField(
            model_name='article',
            name='position',
        ),
    ]
