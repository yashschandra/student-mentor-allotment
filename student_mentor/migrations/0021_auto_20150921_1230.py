# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0020_auto_20150921_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(serialize=False, primary_key=True)),
                ('event_name', models.CharField(max_length=50)),
                ('deadline_mentor', models.DateField(default=datetime.date.today)),
                ('startdate_participant', models.DateField(default=datetime.date.today)),
                ('deadline_participant', models.DateField(default=datetime.date.today)),
                ('on', models.DateField()),
                ('year_cutoff', models.SmallIntegerField(default=5, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('description', models.TextField(blank=True)),
                ('team_event', models.BooleanField(default=False)),
                ('event_type', models.CharField(default=b'Formal', max_length=10, choices=[(b'Informal', b'Informal'), (b'Formal', b'Formal')])),
                ('club', models.ForeignKey(to='student_mentor.Club')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='meeting_participant',
            name='meeting',
        ),
        migrations.DeleteModel(
            name='Meeting_Participant',
        ),
        migrations.RemoveField(
            model_name='meeting_request_participant',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='meeting_request_participant',
            name='participant',
        ),
        migrations.DeleteModel(
            name='Meeting_Request_Participant',
        ),
        migrations.RemoveField(
            model_name='meeting_request_team',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='meeting_request_team',
            name='team',
        ),
        migrations.RemoveField(
            model_name='meeting_team',
            name='meeting',
        ),
        migrations.DeleteModel(
            name='Meeting_Request_Team',
        ),
        migrations.DeleteModel(
            name='Meeting_Team',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='student',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='student',
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
        migrations.RemoveField(
            model_name='team',
            name='mentor',
        ),
        migrations.DeleteModel(
            name='Mentor',
        ),
        migrations.RemoveField(
            model_name='team',
            name='students',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
