# Generated by Django 3.0.6 on 2020-05-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_music'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='song_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]