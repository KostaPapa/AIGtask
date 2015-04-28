# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_auto_20150428_0535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertext',
            name='texts',
        ),
        migrations.RemoveField(
            model_name='usertext',
            name='texts_all',
        ),
        migrations.AddField(
            model_name='usertext',
            name='text',
            field=models.TextField(verbose_name='Dispute Reasons', blank=True),
        ),
    ]
