# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0008_auto_20150428_0532'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserText',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('email', models.OneToOneField(related_name='Email', to='general.Join')),
                ('texts', models.ManyToManyField(to='general.Join', null=True, related_name='Texts')),
                ('texts_all', models.ForeignKey(to='general.Join', related_name='texts_all')),
            ],
        ),
        migrations.RemoveField(
            model_name='usertexts',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usertexts',
            name='texts',
        ),
        migrations.RemoveField(
            model_name='usertexts',
            name='texts_all',
        ),
        migrations.DeleteModel(
            name='UserTexts',
        ),
    ]
