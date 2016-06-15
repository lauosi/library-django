# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20160612_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratebook',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratebook', to='books.Book'),
        ),
        migrations.AlterField(
            model_name='ratebook',
            name='explanation',
            field=models.TextField(default='just because'),
        ),
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='books.Book'),
        ),
    ]
