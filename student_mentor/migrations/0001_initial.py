# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('club_id', models.AutoField(serialize=False, primary_key=True)),
                ('club_name', models.CharField(unique=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Council',
            fields=[
                ('council_id', models.AutoField(serialize=False, primary_key=True)),
                ('council_name', models.CharField(unique=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(serialize=False, primary_key=True)),
                ('event_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('club', models.ForeignKey(to='student_mentor.Club')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='club',
            name='council',
            field=models.ForeignKey(to='student_mentor.Council'),
            preserve_default=True,
        ),
    ]
