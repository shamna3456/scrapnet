from django.db import models
from scrapdealer.models import Scrapdealer
from user_scrap_request.models import UserScrapRequest

class RequestResponce(models.Model):
    request_responce_id = models.AutoField(primary_key=True)
    # scrapdealer_id = models.IntegerField()
    scrapdealer=models.ForeignKey(Scrapdealer,on_delete=models.CASCADE)
    # user_scrap_request_id = models.IntegerField()
    user_scrap_request=models.ForeignKey(UserScrapRequest,on_delete=models.CASCADE)
    responce_details = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    price = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'request_responce'
