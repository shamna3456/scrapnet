from django.db import models
from vehicle.models import Vehicle
from user.models import User


class UserScrapRequest(models.Model):
    user_scrap_request_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # vehicle_id = models.IntegerField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    request_status = models.CharField(max_length=45)
    photo_side1 = models.CharField(max_length=45)
    photo_side2 = models.CharField(max_length=45)
    photo_side3 = models.CharField(max_length=45)
    photo_side4 = models.CharField(max_length=45)
    certificate_no = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user_scrap_request'
