# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0030_meeting_participant_meeting_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='max_participants',
            field=models.SmallIntegerField(default=1),
            preserve_default=True,
        ),
    ]
