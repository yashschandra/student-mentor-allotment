# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0003_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='club',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
