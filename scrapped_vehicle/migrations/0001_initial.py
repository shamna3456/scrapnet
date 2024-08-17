# Generated by Django 3.2.25 on 2024-05-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrappedVehicle',
            fields=[
                ('scrapped_vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'scrapped_vehicle',
                'managed': False,
            },
        ),
    ]