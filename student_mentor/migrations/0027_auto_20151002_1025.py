# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_mentor', '0026_auto_20151002_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting_request_participant',
            name='participant',
        ),
        migrations.RemoveField(
            model_name='meeting_request_team',
            name='team',
        ),
        migrations.AddField(
            model_name='participant',
            name='meeting_request',
            field=models.CharField(default=b'None', max_length=10, choices=[(b'None', b'None'), (b'Accepted', b'Accepted'), (b'Pending', b'Pending')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='meeting_request',
            field=models.CharField(default=b'None', max_length=10, choices=[(b'None', b'None'), (b'Accepted', b'Accepted'), (b'Pending', b'Pending')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meeting_participant',
            name='meeting',
            field=models.OneToOneField(to='student_mentor.Participant'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Meeting_Request_Participant',
        ),
        migrations.AlterField(
            model_name='meeting_team',
            name='meeting',
            field=models.OneToOneField(to='student_mentor.Team'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Meeting_Request_Team',
        ),
    ]
