# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-15 21:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0035_auto_20191013_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='limit_proposal_date',
            field=models.DateField(default=datetime.date(2019, 10, 15), help_text='Limit date to submit talk proposals', verbose_name='Limit Proposals Date'),
            preserve_default=False,
        ),
    ]
