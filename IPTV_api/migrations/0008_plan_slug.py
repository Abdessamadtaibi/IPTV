# Generated by Django 5.1.5 on 2025-03-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPTV_api', '0007_delete_deviceaccess'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
