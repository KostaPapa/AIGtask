# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0010_auto_20150428_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertext',
            name='text',
            field=models.TextField(blank=True, verbose_name='Enter Text'),
        ),
    ]
