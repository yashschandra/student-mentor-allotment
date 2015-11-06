# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0006_auto_20150916_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='year_cutoff',
            field=models.SmallIntegerField(default=5, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
            preserve_default=True,
        ),
    ]
