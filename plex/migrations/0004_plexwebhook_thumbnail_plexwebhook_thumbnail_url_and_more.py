# Generated by Django 4.1 on 2023-08-31 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plex', '0003_plexaccount_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='plexwebhook',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='media/plex_thumbnails/'),
        ),
        migrations.AddField(
            model_name='plexwebhook',
            name='thumbnail_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plexaccount',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='media/plex_account_thumbnails/'),
        ),
    ]
