# Generated by Django 5.1.5 on 2025-03-19 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IPTV_api', '0005_iptvcompress_delete_iptvchannel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='IPTVCompress',
        ),
    ]
