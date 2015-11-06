# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0034_auto_20151004_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='min_participants',
            field=models.SmallIntegerField(default=1),
            preserve_default=True,
        ),
    ]
