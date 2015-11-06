# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0028_auto_20151003_0708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting_participant',
            name='participant',
        ),
        migrations.DeleteModel(
            name='Meeting_Participant',
        ),
        migrations.RemoveField(
            model_name='meeting_team',
            name='team',
        ),
        migrations.DeleteModel(
            name='Meeting_Team',
        ),
    ]
