from django.db import models
from django.contrib import admin
class Bank(models.Model):
        Name=models.CharField(max_length=10)
        Accountno=models.IntegerField(primary_key="accountno")
        Aadharno=models.IntegerField()
        DoB=models.DateField()
        Email=models.EmailField()
        Bank=models.CharField(max_length=21)
class BankAdmin(admin.ModelAdmin):
        list_display=('Name','Accountno','Aadharno','DoB','Email','Bank',)