# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('interaction', models.PositiveIntegerField(verbose_name='interaction', default=0)),
                ('user', models.OneToOneField(related_name='profile', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user',),
                'verbose_name_plural': 'Profiles',
                'verbose_name': 'Profile',
            },
        ),
    ]
