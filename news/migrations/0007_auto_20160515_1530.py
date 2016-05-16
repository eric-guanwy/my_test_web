# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_article_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(upload_to='photos', null=True, verbose_name='upload picture'),
        ),
    ]
