from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    email_id = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    phone_number = models.CharField(db_column='phone number', max_length=45)  # Field renamed to remove unsuitable characters.
    place = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'
