# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0006_remove_museo_num_comen'),
    ]

    operations = [
        migrations.AddField(
            model_name='museo',
            name='num_comen',
            field=models.IntegerField(default=0),
        ),
    ]
