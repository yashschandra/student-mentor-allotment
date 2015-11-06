# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0038_auto_20151005_0935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor_Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deadline_mentor', models.DateTimeField()),
                ('event', models.OneToOneField(to='student_mentor.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='event',
            name='deadline_mentor',
        ),
        migrations.AddField(
            model_name='event',
            name='mentorevent',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='mentor_year_cutoff',
            field=models.SmallIntegerField(default=0, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='participant_year_cutoff',
            field=models.SmallIntegerField(default=5, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
            preserve_default=True,
        ),
    ]
