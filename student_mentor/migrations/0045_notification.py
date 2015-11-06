# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0044_auto_20151015_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.AutoField(serialize=False, primary_key=True)),
                ('notification_type', models.CharField(max_length=20, choices=[(b'mentor event', b'mentor event'), (b'participate in event', b'participate in event'), (b'event rescheduled', b'event rescheduled')])),
                ('message', models.TextField()),
                ('event', models.ForeignKey(to='student_mentor.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
