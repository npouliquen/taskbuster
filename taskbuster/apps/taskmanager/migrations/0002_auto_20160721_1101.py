# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Enter the project name', max_length=100, verbose_name='name')),
                ('color', models.CharField(verbose_name='color', validators=[django.core.validators.RegexValidator('(^#[0-9a-fA-F]{3}$)|(^#[0-9a-fA-F]{6}$)')], help_text='Enter the hex color code, like #ccc or #cccccc', max_length=7, default='#fff')),
                ('user', models.ForeignKey(to='taskmanager.Profile', related_name='projects', verbose_name='user')),
            ],
            options={
                'ordering': ('user', 'name'),
                'verbose_name_plural': 'Projects',
                'verbose_name': 'Project',
            },
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('user', 'name')]),
        ),
    ]
