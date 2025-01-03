# Generated by Django 5.0.1 on 2024-02-02 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_app', '0003_remove_image_title_alter_image_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='image',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos'),
        ),
    ]
