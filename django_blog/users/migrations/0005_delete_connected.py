# Generated by Django 3.2.7 on 2021-09-30 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_connected_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Connected',
        ),
    ]
