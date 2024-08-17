
from django.db import models


class Check(models.Model):
    check_id = models.AutoField(primary_key=True)
    vehicle_no = models.CharField(max_length=45)
    owner_name = models.CharField(max_length=45)
    phone_no = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    vehicle_expiry = models.DateField()
    status = models.CharField(max_length=45)
    suspicious_count = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'check'
