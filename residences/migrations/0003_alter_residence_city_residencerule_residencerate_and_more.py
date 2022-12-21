# Generated by Django 4.1.4 on 2022-12-21 16:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0001_initial'),
        ('residences', '0002_alter_residence_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residence',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_%(class)ss', to='locations.city'),
        ),
        migrations.CreateModel(
            name='ResidenceRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.TimeField(verbose_name='check in time')),
                ('check_out', models.TimeField(verbose_name='check out time')),
                ('text', models.TextField(null=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residence_rules', to='residences.residence')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResidenceRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residence_rates', to='residences.residence')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResidenceComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField()),
                ('status', models.PositiveSmallIntegerField(choices=[(10, 'Created'), (20, 'Approved'), (30, 'Rejected'), (40, 'Deleted')], default=10)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residence_comments', to='residences.residence')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('validated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='validated_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='residencerate',
            constraint=models.UniqueConstraint(fields=('user', 'residence'), name='unique_user_residence_rate'),
        ),
    ]
