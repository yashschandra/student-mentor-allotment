# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0035_event_min_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pending_team',
            name='event',
        ),
        migrations.RemoveField(
            model_name='pending_team',
            name='students',
        ),
        migrations.DeleteModel(
            name='Pending_Team',
        ),
        migrations.AddField(
            model_name='team',
            name='eligible',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='mentor',
            field=models.ForeignKey(to='student_mentor.Mentor', null=True),
            preserve_default=True,
        ),
    ]
