# Generated by Django 3.2.25 on 2024-05-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('email_id', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=45)),
                ('phone_number', models.CharField(db_column='phone number', max_length=45)),
                ('place', models.CharField(max_length=45)),
                ('gender', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
