from django.db import models
from booking.models import Booking

class ScrappedVehicle(models.Model):
    scrapped_vehicle_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'scrapped_vehicle'
