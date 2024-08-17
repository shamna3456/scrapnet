from django.db import models
from scrapped_vehicle.models import ScrappedVehicle
from user.models import User
from scrapdealer.models import Scrapdealer

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    # scrapped_vehicle_id = models.IntegerField()
    scrapped_vehicle=models.ForeignKey(ScrappedVehicle,on_delete=models.CASCADE)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # scrapdealer_id = models.IntegerField()
    scrapdealer = models.ForeignKey(Scrapdealer,on_delete=models.CASCADE)
    amount = models.CharField(max_length=45)
    account_number = models.CharField(max_length=45)
    ifsc = models.CharField(max_length=45)
    status = models.CharField(max_length=45, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'payment'
