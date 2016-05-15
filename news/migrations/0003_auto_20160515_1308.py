# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_testsortable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testsortable',
            name='that',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('position',)},
        ),
        migrations.AddField(
            model_name='article',
            name='position',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Position'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TestSortable',
        ),
    ]
