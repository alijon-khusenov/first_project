# Generated by Django 3.2.8 on 2021-10-20 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_delete_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('client_phone_number', models.CharField(max_length=255, verbose_name='Номер телефона')),
            ],
        ),
    ]
