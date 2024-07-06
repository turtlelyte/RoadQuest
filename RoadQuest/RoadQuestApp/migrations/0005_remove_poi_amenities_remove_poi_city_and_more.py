# Generated by Django 5.0.6 on 2024-07-06 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoadQuestApp', '0004_routeitem_end_lat_routeitem_end_lng_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poi',
            name='amenities',
        ),
        migrations.RemoveField(
            model_name='poi',
            name='city',
        ),
        migrations.RemoveField(
            model_name='poi',
            name='country',
        ),
        migrations.RemoveField(
            model_name='poi',
            name='description',
        ),
        migrations.RemoveField(
            model_name='poi',
            name='last_updated',
        ),
        migrations.RemoveField(
            model_name='poi',
            name='opening_hours',
        ),
        migrations.RemoveField(
            model_name='poi',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='poi',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='poi',
            name='state',
        ),
        migrations.RemoveField(
            model_name='poi',
            name='website',
        ),
        migrations.AlterField(
            model_name='poi',
            name='type',
            field=models.CharField(max_length=255),
        ),
    ]
