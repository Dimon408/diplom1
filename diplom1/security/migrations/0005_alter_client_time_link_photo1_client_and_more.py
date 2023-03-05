# Generated by Django 4.1.2 on 2022-11-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0004_auto_20221015_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_time',
            name='link_photo1_client',
            field=models.ImageField(blank=True, default=None, upload_to='static//photo'),
        ),
        migrations.AlterField(
            model_name='client_time',
            name='link_photo2_client',
            field=models.ImageField(blank=True, default=None, upload_to='static//photo'),
        ),
        migrations.AlterField(
            model_name='client_time',
            name='link_photo3_client',
            field=models.ImageField(blank=True, default=None, upload_to='static//photo'),
        ),
        migrations.AlterField(
            model_name='error',
            name='screen_error',
            field=models.ImageField(blank=True, default=None, upload_to='static//photo'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='link_photo1_worker',
            field=models.ImageField(blank=True, default=None, upload_to='static//photo'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='link_photo2_worker',
            field=models.ImageField(blank=True, default=None, upload_to='static//photo'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='link_photo3_worker',
            field=models.ImageField(blank=True, default=None, upload_to='static//photo'),
        ),
    ]