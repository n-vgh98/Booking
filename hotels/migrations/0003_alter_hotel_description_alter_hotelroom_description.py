# Generated by Django 4.1.4 on 2022-12-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_rename_room_hotelroomfeature_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='hotelroom',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
