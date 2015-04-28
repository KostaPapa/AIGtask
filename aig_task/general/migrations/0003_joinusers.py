# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_auto_20150428_0202'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinUsers',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('email', models.OneToOneField(to='general.Join', related_name='Sharer')),
                ('emailall', models.ForeignKey(to='general.Join', related_name='emailall')),
                ('users', models.ManyToManyField(to='general.Join', blank=True, null=True, related_name='User')),
            ],
        ),
    ]
