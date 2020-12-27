from django.db import models

# Create your models here.
class Patient(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	username = models.CharField(max_length=16)
	password = models.CharField(max_length=16)
	repassword = models.CharField(max_length=16)
	gender = models.CharField(max_length=10)
	phonenumber = models.CharField(max_length=10)

	
	bloodgroup = models.CharField(max_length=5)

	def __str__(self):
		return self.name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name