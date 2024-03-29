# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-29 18:44
from __future__ import unicode_literals

import apps.images.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_registration', '0002_auto_20190827_0824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=apps.images.models.path_and_rename)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='login_registration.User')),
            ],
        ),
    ]
