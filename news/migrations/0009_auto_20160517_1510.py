# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20160515_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_content',
            field=models.TextField(),
        ),
    ]
