# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0045_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='on',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 28, 22, 50, 12, 368968), auto_now_add=True),
            preserve_default=True,
        ),
    ]
