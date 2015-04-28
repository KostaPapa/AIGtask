# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTexts',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('email', models.OneToOneField(related_name='Email', to='general.Join')),
                ('texts', models.ManyToManyField(to='general.Join', related_name='Texts', null=True)),
                ('texts_all', models.ForeignKey(to='general.Join', related_name='texts_all')),
            ],
        ),
        migrations.DeleteModel(
            name='Text',
        ),
    ]
