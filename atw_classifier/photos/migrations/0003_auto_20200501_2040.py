# Generated by Django 3.0.5 on 2020-05-01 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_photo_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
