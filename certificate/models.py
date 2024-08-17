from django.db import models
from RTO.models import Rto
from user.models import User
from vehicle.models import Vehicle
import random
import string



class CertificateRequest(models.Model):
        certificate_request_id = models.AutoField(primary_key=True)
        vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE,null=True)
        user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
        rto = models.ForeignKey(Rto,on_delete=models.CASCADE,null=True)
        status = models.CharField(max_length=45)

        class Meta:
            managed = False
            db_table = 'certificate_request'


class Certificate(models.Model):
    certificate_id = models.AutoField(primary_key=True)
    rto = models.ForeignKey(Rto,on_delete=models.CASCADE,db_column='RTO_id')  # Field name made lowercase.
    holder_name = models.CharField(max_length=45)
    issue_date = models.CharField(max_length=45)
    vehicle_no = models.CharField(max_length=45)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    certificate_no = models.CharField(max_length=45)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE,null=True)
    file = models.CharField(max_length=100)
    # certificate_request_id = models.IntegerField()
    certificate_request=models.ForeignKey(CertificateRequest,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'certificate'


    def save(self, *args, **kwargs):
        if not self.certificate_no:
            # If you want to use random.choice with string.ascii_letters and string.digits
            random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

            self.certificate_no = f"C-{random_string}"

        super().save(*args, **kwargs)
