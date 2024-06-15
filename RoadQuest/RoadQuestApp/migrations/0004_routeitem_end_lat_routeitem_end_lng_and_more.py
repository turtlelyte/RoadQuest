# Generated by Django 5.0.6 on 2024-06-15 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoadQuestApp', '0003_poi'),
    ]

    operations = [
        migrations.AddField(
            model_name='routeitem',
            name='end_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='routeitem',
            name='end_lng',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='routeitem',
            name='start_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='routeitem',
            name='start_lng',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
