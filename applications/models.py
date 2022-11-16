from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    country=models.CharField(max_length=20)
    mobile_no=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    address=models.CharField(max_length=50)

class blog(models.Model):
    # id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=20)
    content=models.TextField()
    