# Generated by Django 4.1.2 on 2022-11-19 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0006_alter_client_time_passport_number_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_time',
            name='phone_number_client',
            field=models.CharField(max_length=255),
        ),
    ]
