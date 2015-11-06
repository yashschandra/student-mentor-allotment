# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0019_auto_20150921_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='club',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='event',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='event',
        ),
        migrations.RemoveField(
            model_name='team',
            name='event',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
