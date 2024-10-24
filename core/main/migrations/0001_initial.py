# Generated by Django 5.1 on 2024-10-13 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='media', verbose_name='page logo')),
                ('name', models.CharField(max_length=20, verbose_name='page name')),
                ('bgimg', models.ImageField(upload_to='media', verbose_name='img')),
                ('tel', models.CharField(max_length=11, verbose_name='tel')),
                ('email', models.CharField(max_length=70, verbose_name='email')),
                ('address', models.CharField(max_length=100, verbose_name='address')),
            ],
        ),
    ]
