# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0004_museo_num_com'),
    ]

    operations = [
        migrations.RenameField(
            model_name='museo',
            old_name='num_com',
            new_name='num_comen',
        ),
    ]
