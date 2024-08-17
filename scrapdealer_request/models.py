from django.db import models
from scrapdealer.models import Scrapdealer
from user_scrap_request.models import UserScrapRequest
from RTO.models import Rto

class ScrapdealerRequest(models.Model):
    scrapdealer_request_id = models.AutoField(primary_key=True)
    #scrapdealer_id = models.IntegerField()
    scrapdealer = models.ForeignKey(Scrapdealer, on_delete=models.CASCADE)
    # user_scrap_request_id = models.IntegerField()
    user_scrap_request = models.ForeignKey(UserScrapRequest, on_delete=models.CASCADE)
    # rto_id = models.IntegerField(db_column='RTO_id')  # Field name made lowercase.
    rto=models.ForeignKey(Rto,on_delete=models.CASCADE)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'scrapdealer_request'

