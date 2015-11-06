# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0033_pending_team_accept'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pending_team',
            old_name='accept',
            new_name='accepted',
        ),
    ]
