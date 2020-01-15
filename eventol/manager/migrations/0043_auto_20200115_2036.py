# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-15 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0042_auto_20200115_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='css_custom',
            field=models.FileField(blank=True, help_text='Custom CSS file for event page', null=True, upload_to='custom_css', verbose_name='Custom CSS'),
        ),
    ]
