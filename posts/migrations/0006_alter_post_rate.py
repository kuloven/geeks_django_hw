# Generated by Django 5.1 on 2024-08-09 13:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rate',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
