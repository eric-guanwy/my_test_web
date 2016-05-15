# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20160515_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_content',
            field=tinymce.models.HTMLField(),
        ),
    ]
