# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Escogido',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('usuario', models.CharField(max_length=32)),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('usuario', models.CharField(max_length=32)),
                ('letra', models.CharField(blank=True, null=True, max_length=64)),
                ('color', models.CharField(max_length=32)),
                ('titulo', models.CharField(default='', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Museo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('idmuseo', models.IntegerField()),
                ('nombre', models.CharField(max_length=32)),
                ('descripcion_entidad', models.TextField()),
                ('horario', models.TextField()),
                ('transporte', models.TextField()),
                ('accesibilidad', models.IntegerField(choices=[(0, '0'), (1, '1')])),
                ('content_URL', models.URLField(max_length=300)),
                ('nombre_via', models.CharField(max_length=64)),
                ('clase_via', models.CharField(max_length=64)),
                ('tipo_num', models.CharField(max_length=64)),
                ('numero', models.CharField(max_length=64)),
                ('localidad', models.CharField(max_length=64)),
                ('provincia', models.CharField(max_length=64)),
                ('codigo_postal', models.TextField()),
                ('barrio', models.CharField(max_length=64)),
                ('distrito', models.CharField(max_length=64)),
                ('coordenada_x', models.PositiveIntegerField()),
                ('coordenada_y', models.PositiveIntegerField()),
                ('latitud', models.FloatField(blank=True, null=True)),
                ('longitud', models.FloatField(blank=True, null=True)),
                ('telefono', models.TextField()),
                ('fax', models.TextField()),
                ('email', models.TextField()),
                ('tipo', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='escogido',
            name='museo',
            field=models.ForeignKey(to='museos.Museo'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='museo',
            field=models.ForeignKey(to='museos.Museo'),
        ),
    ]
