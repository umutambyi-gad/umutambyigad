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


	class Meta:
		verbose_name_plural = 'Introduction'


class Profile(models.Model):
	avatar = models.ImageField(upload_to='images')
	names = models.CharField(max_length=250)
	profile = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	phone = models.CharField(max_length=250)
	about =  models.TextField()
	added_date = models.DateTimeField(auto_now_add=True)


	# This method will avoid to allow more than one instance being saved
	def save(self, *args, **kwargs):
		if not self.pk and Introduction.objects.exists():
			return False
		super().save(*args, **kwargs)


	def __str__(self):
		return self.names


	class Meta:
		verbose_name_plural = 'Profile'


class Skills(models.Model):
	name = models.CharField(max_length=250)
	rate = models.IntegerField(default=0)
	added_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.name


	class Meta:
		verbose_name_plural = 'Skills'


class ServiceSection(models.Model):
	heading = models.CharField(max_length=250)
	paragraph = models.TextField()
	added_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.heading


	class Meta:
		verbose_name_plural = 'Service section'


class Sevices(models.Model):
	icon = models.CharField(max_length=200)
	title = = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	added_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title


	class Meta:
		verbose_name_plural = 'Services'
