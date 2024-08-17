from django.db import models


class Rto(models.Model):
    rto_id = models.AutoField(db_column='RTO_id', primary_key=True,null=False)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    place = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    rto_office_name = models.CharField(db_column='RTO_office_name', max_length=45)  # Field name made lowercase.
    phone = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'RTO'
