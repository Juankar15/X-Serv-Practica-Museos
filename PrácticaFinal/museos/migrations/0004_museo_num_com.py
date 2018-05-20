# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0003_remove_estilo_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='museo',
            name='num_com',
            field=models.IntegerField(default=0),
        ),
    ]
