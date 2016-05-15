# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20160515_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(default=datetime.datetime(2016, 5, 15, 14, 13, 51, 540956, tzinfo=utc), upload_to='photos', verbose_name='upload picture'),
            preserve_default=False,
        ),
    ]
