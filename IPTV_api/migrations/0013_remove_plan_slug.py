# Generated by Django 5.1.5 on 2025-03-28 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IPTV_api', '0012_alter_plan_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='slug',
        ),
    ]
