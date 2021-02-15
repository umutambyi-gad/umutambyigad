from django.db import models


# Create your models here.
class Careers(models.Model):
	career = models.CharField(max_length=250)
	added_date = models.DateTimeField(auto_now_add=True)
	

	def __str__(self):
		return self.career


class Introduction(models.Model):
	username = models.CharField(max_length=200)
	background_image = models.ImageField(upload_to='images')
	salutation = models.CharField(max_length=250)
	about = models.CharField(max_length=300)
	careers = models.ManyToManyField(Careers)
	added_date = models.DateTimeField(auto_now_add=True)


	# This method will avoid to allow more than one instance being saved
	def save(self, *args, **kwargs):
		if not self.pk and Introduction.objects.exists():
			return False
		super().save(*args, **kwargs)


	def __str__(self):
		return self.username

