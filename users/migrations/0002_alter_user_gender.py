# Generated by Django 4.1.4 on 2022-12-13 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(1, 'male'), (2, 'female')], null=True),
        ),
    ]
