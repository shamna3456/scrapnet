# Generated by Django 3.2.25 on 2024-05-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserScrapRequest',
            fields=[
                ('user_scrap_request_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=45)),
                ('time', models.CharField(max_length=45)),
                ('request_status', models.CharField(max_length=45)),
                ('photo_side1', models.CharField(max_length=45)),
                ('photo_side2', models.CharField(max_length=45)),
                ('photo_side3', models.CharField(max_length=45)),
                ('photo_side4', models.CharField(max_length=45)),
                ('certificate_no', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'user_scrap_request',
                'managed': False,
            },
        ),
    ]
