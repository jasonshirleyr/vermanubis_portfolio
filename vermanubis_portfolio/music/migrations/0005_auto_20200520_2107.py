# Generated by Django 3.0.6 on 2020-05-20 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20200520_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about',
            field=models.TextField(max_length=10000),
        ),
    ]
