# Generated by Django 4.0.1 on 2022-02-06 01:10

from django.db import migrations, models
import loadImage.models


class Migration(migrations.Migration):

    dependencies = [
        ('loadImage', '0004_alter_loadimagemodel_name_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadimagemodel',
            name='name_image',
            field=models.ImageField(blank='', default='', upload_to='img'),
        ),
    ]
