# Generated by Django 5.1.5 on 2025-03-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPTV_api', '0013_remove_plan_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
