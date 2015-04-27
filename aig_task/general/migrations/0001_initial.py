# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('ref_id', models.CharField(default='ABC', max_length=120)),
                ('ip_address', models.CharField(default='ABC', max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='join',
            unique_together=set([('email', 'ref_id')]),
        ),
    ]
