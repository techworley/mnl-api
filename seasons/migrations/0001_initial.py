# Generated by Django 2.0 on 2018-02-12 02:53

import django.contrib.postgres.fields.ranges
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', django.contrib.postgres.fields.ranges.DateRangeField()),
            ],
        ),
    ]
