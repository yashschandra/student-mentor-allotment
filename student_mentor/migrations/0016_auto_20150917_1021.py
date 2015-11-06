# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0015_auto_20150917_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting_Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting_Request_Participant',
            fields=[
                ('meeting_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting_Request_Team',
            fields=[
                ('meeting_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting_Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('meeting', models.OneToOneField(to='student_mentor.Meeting_Request_Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('mentor_id', models.AutoField(serialize=False, primary_key=True)),
                ('event', models.ForeignKey(to='student_mentor.Event')),
                ('student', models.ForeignKey(to='student_mentor.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('participant_id', models.AutoField(serialize=False, primary_key=True)),
                ('event', models.ForeignKey(to='student_mentor.Event')),
                ('mentor', models.ForeignKey(to='student_mentor.Mentor')),
                ('student', models.ForeignKey(to='student_mentor.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(serialize=False, primary_key=True)),
                ('team_name', models.CharField(max_length=30)),
                ('event', models.ForeignKey(to='student_mentor.Event')),
                ('mentor', models.ForeignKey(to='student_mentor.Mentor')),
                ('students', models.ManyToManyField(to='student_mentor.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='meeting_request_team',
            name='mentor',
            field=models.ForeignKey(to='student_mentor.Mentor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meeting_request_team',
            name='team',
            field=models.ForeignKey(to='student_mentor.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meeting_request_participant',
            name='mentor',
            field=models.ForeignKey(to='student_mentor.Mentor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meeting_request_participant',
            name='participant',
            field=models.ForeignKey(to='student_mentor.Participant'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meeting_participant',
            name='meeting',
            field=models.OneToOneField(to='student_mentor.Meeting_Request_Participant'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(default=b'Formal', max_length=10, choices=[(b'Informal', b'Informal'), (b'Formal', b'Formal')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='team_event',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='clubs',
            field=models.ManyToManyField(to='student_mentor.Club'),
            preserve_default=True,
        ),
    ]
