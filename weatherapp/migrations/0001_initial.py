# Generated by Django 3.2.9 on 2021-11-16 13:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('cities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=40), blank=True, default=['São Paulo'], size=None)),
            ],
        ),
    ]
