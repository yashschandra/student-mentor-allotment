# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0024_auto_20151001_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='deadline_mentor',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='deadline_participant',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='on',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='startdate_participant',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
