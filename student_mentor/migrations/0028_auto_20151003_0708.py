# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0027_auto_20151002_1025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting_participant',
            old_name='meeting',
            new_name='participant',
        ),
        migrations.RenameField(
            model_name='meeting_team',
            old_name='meeting',
            new_name='team',
        ),
    ]
