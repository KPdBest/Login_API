from django.db import models

class Sudo(models.Model):
   Fname=models.CharField(max_length=100)
   Fa_Name=models.CharField(max_length=100)
   Mobile_no=models.CharField(max_length=100)
   Fa_Mobile_no=models.CharField(max_length=100)
   Email=models.CharField(max_length=100)
   Gender=models.CharField(max_length=20)



class User(models.Model):

	link=models.ForeignKey(Sudo, on_delete=models.CASCADE)
	Email=models.CharField(max_length=100)
	Password=models.CharField(max_length=100)
   