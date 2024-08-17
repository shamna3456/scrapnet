from django.db import models

# Create your models here.

class StationVehicle(models.Model):
    station_vehicle_id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=45)
    vehicle_num = models.CharField(max_length=45)
    photo = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    starting_date = models.DateField()
    expiry_date = models.DateField()
    police_station_id = models.IntegerField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'station_vehicle'
