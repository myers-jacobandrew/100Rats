# Generated by Django 5.0.1 on 2024-02-23 02:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0008_alter_monster_challenge_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
