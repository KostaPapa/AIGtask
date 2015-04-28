# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_auto_20150428_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='user',
            field=models.ForeignKey(to='general.Join', blank=True, null=True, related_name='referal'),
        ),
    ]
