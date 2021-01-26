# Generated by Django 3.1.5 on 2021-01-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridges', '0002_auto_20210122_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bridge',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='bridge',
            name='width',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
