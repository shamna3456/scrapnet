# Generated by Django 3.2.25 on 2024-06-05 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('check_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_no', models.CharField(max_length=45)),
                ('owner_name', models.CharField(max_length=45)),
                ('phone_no', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('vehicle_expiry', models.DateField()),
                ('status', models.CharField(max_length=45)),
                ('suspicious_count', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'check',
                'managed': False,
            },
        ),
    ]
