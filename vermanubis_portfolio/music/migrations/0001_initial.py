# Generated by Django 3.0.6 on 2020-05-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=1000)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
