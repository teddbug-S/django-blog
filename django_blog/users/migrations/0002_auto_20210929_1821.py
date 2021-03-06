# Generated by Django 3.2.7 on 2021-09-29 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=250, null=True, verbose_name='biography'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='display_picture',
            field=models.ImageField(default='avatar.jpg', upload_to='profile_pics'),
        ),
    ]
