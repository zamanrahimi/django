# Generated by Django 4.0.3 on 2022-04-02 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_destination_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='test',
        ),
    ]