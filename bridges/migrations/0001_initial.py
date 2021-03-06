# Generated by Django 3.1.5 on 2021-02-07 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='bridge height')),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='bridge width')),
                ('latitude_north', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='bounding box north latitude')),
                ('latitude_south', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='bounding box south latitude')),
                ('longitude_west', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='bounding box west longitude')),
                ('longitude_east', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='bounding box east longitude')),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='bounding box center latitude')),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='bounding box center longitude')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='date of creation')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='date of last update')),
            ],
            options={
                'verbose_name': 'bridge',
                'verbose_name_plural': 'bridges',
            },
        ),
        migrations.CreateModel(
            name='BridgeUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('bridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bridge_updates', to='bridges.bridge', verbose_name='updated bridge')),
            ],
        ),
    ]
