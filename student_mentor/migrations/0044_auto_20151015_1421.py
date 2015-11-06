# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0043_auto_20151014_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='danger_team',
            name='students',
        ),
        migrations.RemoveField(
            model_name='danger_team',
            name='team',
        ),
        migrations.DeleteModel(
            name='Danger_Team',
        ),
    ]
