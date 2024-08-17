from django.db import models


class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    u_id = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'login'
