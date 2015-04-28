# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0011_auto_20150428_0549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertext',
            name='email',
        ),
        migrations.AddField(
            model_name='join',
            name='text',
            field=models.TextField(verbose_name='Enter Text', blank=True),
        ),
        migrations.DeleteModel(
            name='UserText',
        ),
    ]
