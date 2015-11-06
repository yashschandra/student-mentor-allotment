# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0018_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='deadline',
        ),
        migrations.AddField(
            model_name='event',
            name='deadline_mentor',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='deadline_participant',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='startdate_participant',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
    ]
