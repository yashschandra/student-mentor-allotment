# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0031_event_max_participants'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pending_Team',
            fields=[
                ('team_id', models.AutoField(serialize=False, primary_key=True)),
                ('team_name', models.CharField(max_length=30)),
                ('event', models.ForeignKey(to='student_mentor.Event')),
                ('students', models.ManyToManyField(to='student_mentor.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
