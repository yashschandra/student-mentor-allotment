# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0025_auto_20151002_0711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting_request_participant',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='meeting_request_team',
            name='mentor',
        ),
    ]
