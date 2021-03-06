# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-09 06:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_client_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128, verbose_name='nome')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('is_active', models.BooleanField(default=True, verbose_name='ativo')),
            ],
        ),
    ]
