from django.db import models
from policestationn.models import PoliceStation
from vehicle.models import Vehicle

class SuspiciousActivity(models.Model):
    suspicious_activity_id = models.AutoField(primary_key=True)
    # police_station=models.ForeignKey()
    police_station=models.ForeignKey(PoliceStation,on_delete=models.CASCADE)
    # vehicle_id = models.IntegerField()
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    case_no = models.CharField(max_length=45)
    case_details = models.CharField(max_length=45)
    case_date = models.DateField()


    class Meta:
        managed = False
        db_table = 'suspicious_activity'
