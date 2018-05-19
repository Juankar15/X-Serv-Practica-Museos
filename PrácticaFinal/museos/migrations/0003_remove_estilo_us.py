# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0002_estilo_us'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estilo',
            name='us',
        ),
    ]
