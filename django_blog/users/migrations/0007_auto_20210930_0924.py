# Generated by Django 3.2.7 on 2021-09-30 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_connected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connected',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='connected',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='connected',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='connected',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='connected',
            name='youtube',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='biography'),
        ),
    ]