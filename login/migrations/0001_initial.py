# Generated by Django 3.2.25 on 2024-05-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('type', models.CharField(max_length=45)),
                ('u_id', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'login',
                'managed': False,
            },
        ),
    ]