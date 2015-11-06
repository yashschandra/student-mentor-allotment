# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0014_auto_20150917_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.SmallIntegerField(default=1),
            preserve_default=True,
        ),
    ]
