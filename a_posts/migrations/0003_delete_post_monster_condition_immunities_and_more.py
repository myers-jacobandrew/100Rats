# Generated by Django 5.0.1 on 2024-01-22 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0002_monster'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='monster',
            name='condition_immunities',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='special_abilities_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='monster',
            name='armor_class',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='monster',
            name='challenge_rating',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='monster',
            name='charisma',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='monster',
            name='constitution',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='monster',
            name='dexterity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='monster',
            name='experience_points',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='monster',
            name='hit_points',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='monster',
            name='intelligence',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='monster',
            name='strength',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='monster',
            name='wisdom',
            field=models.IntegerField(null=True),
        ),
    ]
