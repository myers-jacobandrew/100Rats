# Generated by Django 5.0.1 on 2024-02-23 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0007_alter_monster_actions_alter_monster_alignment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='challenge_rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]