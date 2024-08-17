from django.db import models
from request_responce.models import RequestResponce
from user.models import User
from vehicle.models import Vehicle
from scrapdealer.models import Scrapdealer

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    # request_responce_id = models.IntegerField()
    request_response=models.ForeignKey(RequestResponce,on_delete=models.CASCADE)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # vehicle_id = models.CharField(max_length=45)
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=45)
    scrapdealer=models.ForeignKey(Scrapdealer,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'booking'
