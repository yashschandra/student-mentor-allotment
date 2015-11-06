# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0029_auto_20151003_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting_Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('place', models.CharField(max_length=30)),
                ('participant', models.OneToOneField(to='student_mentor.Participant')),
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
                ('place', models.CharField(max_length=30)),
                ('team', models.OneToOneField(to='student_mentor.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
