# Generated by Django 3.1.5 on 2021-01-22 01:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bridges', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bridge',
            name='update',
        ),
        migrations.AddField(
            model_name='bridge',
            name='last_contributor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_contributor_bridges', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bridge',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='bridge',
            name='latitude',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bridge',
            name='longitute',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bridge',
            name='width',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]