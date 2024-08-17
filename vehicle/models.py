from django.db import models
from user.models import User

class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_name = models.CharField(max_length=45)
    vehicle_number = models.CharField(max_length=45)
    colour = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    owner_name = models.CharField(max_length=45)
    owner_contact = models.CharField(max_length=45)
    insurance_details = models.CharField(max_length=45)
    registration_date = models.DateField()
    last_service_date = models.DateField()
    mileage = models.CharField(max_length=45)
    pollution_certificate = models.CharField(max_length=45)
    engine_number = models.CharField(max_length=45)
    photo = models.CharField(max_length=45)
    user_id = models.IntegerField()
    expiry_date = models.DateField()
    status = models.CharField(max_length=45)
    vehicle_type = models.CharField(db_column='vehicle type', max_length=45)
    class Meta:
        managed = False
        db_table = 'vehicle'

