from django.db import models

# Create your models here.
"""
界面显示的字段    
做业务罗判断   状态
设计固定的  主键   外键
"""


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=64, unique=True, db_index=True)
    password = models.CharField(max_length=128)
    contacts = models.CharField(max_length=64, null=True)
    company = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=11)
    qq = models.CharField(max_length=15)
    head = models.CharField(max_length=100)
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'account'
