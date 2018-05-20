# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0007_museo_num_comen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='museo',
            name='num_comen',
        ),
    ]
