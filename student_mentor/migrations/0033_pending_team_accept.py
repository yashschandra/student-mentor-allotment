# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0032_pending_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='pending_team',
            name='accept',
            field=models.SmallIntegerField(default=1),
            preserve_default=True,
        ),
    ]
