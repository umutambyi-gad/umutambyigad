from django.db import models


# Create your models here.
class Careers(models.Model):
	career = models.CharField(max_length=250)


class Introduction(models.Model):
	background_image = models.ImageField(upload_to='images')
	salutation = models.CharField(max_length=250)
	names = models.CharField(max_length=300)
	careers = models.ManyToManyField(Careers)
	added_date = models.DateTimeField(auto_now_add=True)

