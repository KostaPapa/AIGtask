# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_joinusers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinusers',
            name='email',
        ),
        migrations.RemoveField(
            model_name='joinusers',
            name='emailall',
        ),
        migrations.RemoveField(
            model_name='joinusers',
            name='users',
        ),
        migrations.DeleteModel(
            name='JoinUsers',
        ),
    ]
