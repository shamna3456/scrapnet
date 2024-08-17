# Generated by Django 3.2.25 on 2024-05-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestResponce',
            fields=[
                ('request_responce_id', models.AutoField(primary_key=True, serialize=False)),
                ('responce_details', models.CharField(max_length=45)),
                ('status', models.CharField(max_length=45)),
                ('price', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'request_responce',
                'managed': False,
            },
        ),
    ]