# Generated by Django 3.2.25 on 2024-05-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scrapdealer',
            fields=[
                ('scrapdealer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('place', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('lisence', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('start_time', models.CharField(max_length=45)),
                ('end_time', models.CharField(max_length=45)),
                ('service_provided', models.CharField(max_length=45)),
                ('status', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'scrapdealer',
                'managed': False,
            },
        ),
    ]