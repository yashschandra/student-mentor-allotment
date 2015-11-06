# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0004_auto_20150916_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(serialize=False, primary_key=True)),
                ('event_name', models.CharField(max_length=50)),
                ('deadline', models.DateTimeField()),
                ('on', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('club', models.ForeignKey(to='student_mentor.Club')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
