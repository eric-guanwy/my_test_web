# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSortable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.PositiveSmallIntegerField(verbose_name='Position')),
                ('test_char', models.CharField(max_length=5)),
                ('that', models.ForeignKey(to='news.Article')),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]
