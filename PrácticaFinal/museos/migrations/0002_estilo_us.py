# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('museos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estilo',
            name='us',
            field=models.OneToOneField(default='', to=settings.AUTH_USER_MODEL),
        ),
    ]
