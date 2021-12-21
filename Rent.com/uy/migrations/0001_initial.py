# Generated by Django 3.2.9 on 2021-12-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New_home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('region', models.CharField(max_length=150)),
                ('district', models.CharField(max_length=150)),
                ('cost', models.CharField(max_length=100)),
                ('number_of_rooms', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('img_1', models.ImageField(upload_to='home_images/')),
                ('img_2', models.ImageField(upload_to='home_images/')),
                ('img_3', models.ImageField(upload_to='home_images/')),
            ],
            options={
                'verbose_name': 'home',
                'verbose_name_plural': 'homes',
            },
        ),
    ]