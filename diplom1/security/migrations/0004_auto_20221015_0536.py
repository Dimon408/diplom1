# Generated by Django 2.2.12 on 2022-10-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0003_auto_20221015_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='screen_error',
            field=models.ImageField(blank=True, default=None, upload_to='error_img'),
        ),
    ]
