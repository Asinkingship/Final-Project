# Generated by Django 4.2.16 on 2024-10-30 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.CharField(max_length=200),
        ),
    ]
