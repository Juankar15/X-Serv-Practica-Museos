# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0005_auto_20180520_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='museo',
            name='num_comen',
        ),
    ]
