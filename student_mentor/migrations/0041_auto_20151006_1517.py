# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0040_auto_20151006_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='mentor',
            field=models.ForeignKey(to='student_mentor.Mentor', null=True),
            preserve_default=True,
        ),
    ]
