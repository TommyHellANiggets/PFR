# Generated by Django 5.0.3 on 2024-03-28 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0002_alter_fuel_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='fuel',
            name='cropping',
        ),
        migrations.RemoveField(
            model_name='fuel',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='fuel',
            name='photo_height',
        ),
        migrations.RemoveField(
            model_name='fuel',
            name='photo_width',
        ),
        migrations.AddField(
            model_name='fuel',
            name='photo_url',
            field=models.URLField(blank=True),
        ),
    ]
