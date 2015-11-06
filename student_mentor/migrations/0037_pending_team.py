# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0036_auto_20151004_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pending_Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=30)),
                ('event', models.ForeignKey(to='student_mentor.Event')),
                ('students', models.ManyToManyField(to='student_mentor.Student')),
                ('team', models.OneToOneField(to='student_mentor.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
