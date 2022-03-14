from datetime import timezone
from django.db import models


class User(models.Model):
    name=models.CharField(max_length=80)
    surname=models.CharField(max_length=80)
    email=models.EmailField(max_length=80)
    telephone_no=models.CharField(max_length=20)
    password=models.CharField(max_length=100)

class Cargo(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    source_address=models.CharField(max_length=80)
    destination_addresss=models.CharField(max_length=80)
    sending_date=models.DateTimeField()
    arrival_date=models.DateTimeField()




    