# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0041_auto_20151006_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Danger_Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('left', models.IntegerField(default=1)),
                ('students', models.ManyToManyField(to='student_mentor.Student')),
                ('team', models.OneToOneField(to='student_mentor.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
