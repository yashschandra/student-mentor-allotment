# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0042_danger_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='danger_team',
            name='left',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
