# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0037_pending_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('min_participants', models.SmallIntegerField()),
                ('max_participants', models.SmallIntegerField()),
                ('event', models.OneToOneField(to='student_mentor.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='event',
            old_name='team_event',
            new_name='teamevent',
        ),
        migrations.RemoveField(
            model_name='event',
            name='max_participants',
        ),
        migrations.RemoveField(
            model_name='event',
            name='min_participants',
        ),
    ]
