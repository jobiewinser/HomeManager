# Generated by Django 4.1 on 2023-08-31 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlexAccount',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.basemodel')),
                ('plex_id', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('thumnail_url', models.TextField(blank=True, null=True)),
            ],
            bases=('home.basemodel',),
        ),
        migrations.CreateModel(
            name='PlexWebhook',
            fields=[
                ('webhook_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.webhook')),
                ('plex_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plex.plexaccount')),
            ],
            bases=('home.webhook',),
        ),
    ]