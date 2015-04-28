# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_join_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='user',
        ),
    ]
