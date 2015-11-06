# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0005_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='deadline',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
