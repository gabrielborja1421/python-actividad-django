# Generated by Django 4.0.1 on 2022-02-07 06:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('primerComponente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='segundomodelo',
            name='edited',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='segundomodelo',
            name='create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
