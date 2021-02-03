# Generated by Django 3.1.5 on 2021-02-03 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import vehicles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=None, max_length=200, null=True, verbose_name='vehicle name')),
                ('gross_weight', models.IntegerField(blank=True, null=True, verbose_name='vehicle gross weight')),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='vehicle height')),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='vehicle width')),
                ('length', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='vehicle length')),
                ('has_hazardous_goods', models.BooleanField(default=False, verbose_name='has hazardous goods')),
                ('tunnel_category', models.CharField(choices=[('X', 'No tunnel category'), ('A', 'Tunnel category A'), ('B', 'Tunnel category B'), ('C', 'Tunnel category C'), ('D', 'Tunnel category D'), ('E', 'Tunnel category E')], default='X', max_length=1, verbose_name='vehicle tunnel category')),
                ('truck_type', models.CharField(choices=[('C', 'Car'), ('S', 'Straight truck'), ('T', 'Tractor truck')], default='S', max_length=1, verbose_name='vehicle type')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='vehicle creation date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='last vehicle update date')),
                ('image', models.ImageField(blank=True, max_length=255, upload_to=vehicles.models.get_vehicle_path, verbose_name='vehicle image')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicles', to=settings.AUTH_USER_MODEL, verbose_name='vehicle owner')),
            ],
            options={
                'verbose_name': 'vehicle',
                'verbose_name_plural': 'vehicles',
            },
        ),
    ]
