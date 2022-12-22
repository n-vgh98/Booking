# Generated by Django 4.1.4 on 2022-12-22 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('is_valid', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('registration_code', models.CharField(max_length=64)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terminal_city_%(class)s', to='locations.city')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TerminalAirport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(default=1)),
                ('is_valid', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terminal_airport', to='flights.airport')),
            ],
        ),
        migrations.CreateModel(
            name='FlightTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.SmallIntegerField(default=1)),
                ('origin_time', models.TimeField()),
                ('destination_time', models.TimeField()),
                ('is_valid', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('type', models.BooleanField(choices=[(1, 'systemic'), (0, 'charter')], default=1)),
                ('flight_class', models.PositiveSmallIntegerField(choices=[(1, 'economy'), (2, 'business')])),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='destination_flight_airport', to='flights.airport')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='origin_flight_airport', to='flights.airport')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]