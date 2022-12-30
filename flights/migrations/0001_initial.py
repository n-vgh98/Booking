# Generated by Django 4.1.4 on 2022-12-30 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('currencies', '0001_initial'),
        ('locations', '0002_alter_country_name_city_unique_city_province_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirlineCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('is_valid', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
            ],
        ),
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
            name='FlightPassengerReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=16)),
                ('last_name', models.CharField(max_length=32)),
                ('national_id', models.PositiveIntegerField()),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, ' male'), (2, 'female')], default=1)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('date_birth', models.DateField()),
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
                ('date_of_departure', models.DateField()),
                ('time_of_departure', models.TimeField()),
                ('price', models.FloatField()),
                ('is_valid', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('type', models.BooleanField(choices=[(1, 'systemic'), (0, 'charter')], default=1)),
                ('flight_class', models.PositiveSmallIntegerField(choices=[(1, 'economy'), (2, 'business'), (3, 'first')])),
                ('flight_number', models.PositiveSmallIntegerField()),
                ('luggage_allowance', models.PositiveSmallIntegerField(default=20)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_airline', to='flights.airlinecompany')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='price_currency_flight_tickets', to='currencies.currency')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='destination_flight_airport', to='flights.airport')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='origin_flight_airport', to='flights.airport')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FlightReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='flight_reservations', to='flights.flightticket')),
                ('passenger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='flight_reservation_passenger', to='flights.flightpassengerreservation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_reservations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
