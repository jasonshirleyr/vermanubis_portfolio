# Generated by Django 3.0.6 on 2020-05-20 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_player_url', models.URLField(blank=True)),
                ('bandcamp_url', models.URLField(blank=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
