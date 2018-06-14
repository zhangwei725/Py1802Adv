from django.db import models


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, db_index=True, unique=True)
    password = models.CharField(max_length=64)
    sex = models.IntegerField()
    phone = models.CharField(max_length=11, default='110')

    class Meta:
        db_table = 'tb_user'
