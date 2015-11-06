# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student_mentor', '0011_auto_20150917_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(serialize=False, primary_key=True)),
                ('year', models.SmallIntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('student_name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=15, choices=[(b'CERAMIC', b'CERAMIC'), (b'COMPUTER SCIENCE', b'COMPUTER SCIENCE'), (b'CIVIL', b'CIVIL'), (b'ELECTRICAL', b'ELECTRICAL'), (b'ELECTRONICS', b'ELECTRONICS'), (b'METALURGICAL', b'METALURGICAL'), (b'MINING', b'MINING'), (b'MECHANICAL', b'MECHANICAL'), (b'CHEMICAL', b'CHEMICAL'), (b'BIOMEDICAL', b'BIOMEDICAL'), (b'MATHEMATICS N COMPUTING', b'MATHEMATICS N COMPUTING'), (b'APPLIED CHEMISTRY', b'APPLIED CHEMISTRY'), (b'APPLIED MATHEMATICS', b'APPLIED MATHEMATICS'), (b'APPLIED PHYSICS', b'APPLIED PHYSICS'), (b'MATERIAL SCIENCE', b'MATERIAL SCIENCE'), (b'PHARMACEUTICS', b'PHARMACEUTICS')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
