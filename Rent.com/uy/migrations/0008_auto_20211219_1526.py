# Generated by Django 3.2.9 on 2021-12-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uy', '0007_alter_new_home_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_home',
            name='user',
        ),
        migrations.AddField(
            model_name='new_home',
            name='user',
            field=models.ManyToManyField(blank=True, to='uy.Profile'),
        ),
    ]