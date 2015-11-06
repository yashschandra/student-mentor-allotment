# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0039_auto_20151006_0810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='mentor_year_cutoff',
        ),
        migrations.AddField(
            model_name='mentor_event',
            name='mentor_year_cutoff',
            field=models.SmallIntegerField(default=2, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='mentorevent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='participant_year_cutoff',
            field=models.SmallIntegerField(default=5, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
            preserve_default=True,
        ),
    ]
