# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0022_auto_20150921_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='year_cutoff',
            new_name='participant_year_cutoff',
        ),
        migrations.AddField(
            model_name='event',
            name='mentor_year_cutoff',
            field=models.SmallIntegerField(default=2, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
            preserve_default=True,
        ),
    ]
