# Generated by Django 4.1.4 on 2022-12-21 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('hotels', '0003_alter_hotel_description_alter_hotelroom_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels_city', to='locations.city'),
        ),
    ]
