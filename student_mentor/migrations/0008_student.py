# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('student_mentor', '0007_event_year_cutoff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(serialize=False, primary_key=True)),
                ('year', models.SmallIntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('user', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('student_name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=15, choices=[(b'CERAMIC', b'CERAMIC'), (b'COMPUTER SCIENCE', b'COMPUTER SCIENCE'), (b'CIVIL', b'CIVIL'), (b'ELECTRICAL', b'ELECTRICAL'), (b'ELECTRONICS', b'ELECTRONICS'), (b'METALURGICAL', b'METALURGICAL'), (b'MINING', b'MINING'), (b'MECHANICAL', b'MECHANICAL'), (b'CHEMICAL', b'CHEMICAL'), (b'BIOMEDICAL', b'BIOMEDICAL'), (b'MATHEMATICS N COMPUTING', b'MATHEMATICS N COMPUTING'), (b'APPLIED CHEMISTRY', b'APPLIED CHEMISTRY'), (b'APPLIED MATHEMATICS', b'APPLIED MATHEMATICS'), (b'APPLIED PHYSICS', b'APPLIED PHYSICS'), (b'MATERIAL SCIENCE', b'MATERIAL SCIENCE'), (b'PHARMACEUTICS', b'PHARMACEUTICS')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
