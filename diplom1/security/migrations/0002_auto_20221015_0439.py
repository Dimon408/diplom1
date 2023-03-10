# Generated by Django 2.2.12 on 2022-10-15 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_time',
            name='link_photo1_client',
            field=models.ImageField(blank=True, default=None, upload_to='client_img'),
        ),
        migrations.AlterField(
            model_name='client_time',
            name='link_photo2_client',
            field=models.ImageField(blank=True, default=None, upload_to='client_img'),
        ),
        migrations.AlterField(
            model_name='client_time',
            name='link_photo3_client',
            field=models.ImageField(blank=True, default=None, upload_to='client_img'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='link_photo1_worker',
            field=models.ImageField(blank=True, default=None, upload_to='client_img'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='link_photo2_worker',
            field=models.ImageField(blank=True, default=None, upload_to='client_img'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='link_photo3_worker',
            field=models.ImageField(blank=True, default=None, upload_to='client_img'),
        ),
    ]
