from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Introduction(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	background_image = models.ImageField(upload_to='images')
	salutation = models.CharField(max_length=250)
	about = models.CharField(max_length=300)
	added_date = models.DateTimeField(auto_now_add=True)


	# This method will avoid to allow more than one instance being saved
	def save(self, *args, **kwargs):
		if not self.pk and Introduction.objects.exists():
			return False
		super().save(*args, **kwargs)


	def __str__(self):
		return self.user.username


	class Meta:
		verbose_name_plural = 'Introduction'


class Careers(models.Model):
	career = models.CharField(max_length=250)
	added_date = models.DateTimeField(auto_now_add=True)
	

	def __str__(self):
		return self.career

	class Meta:
		verbose_name_plural = 'Careers'



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
		if not self.pk and Profile.objects.exists():
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


	# This method will avoid to allow more than one instance being saved
	def save(self, *args, **kwargs):
		if not self.pk and ServiceSection.objects.exists():
			return False
		super().save(*args, **kwargs)


	def __str__(self):
		return self.heading


	class Meta:
		verbose_name_plural = 'Service section'


class Services(models.Model):
	icon = models.CharField(max_length=200)
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	added_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title


	class Meta:
		verbose_name_plural = 'Services'


class StatisticSection(models.Model):
	background_image = models.ImageField(upload_to='images')
	added_date = models.DateTimeField(auto_now_add=True)


	# This method will avoid to allow more than one instance being saved
	def save(self, *args, **kwargs):
		if not self.pk and StatisticSection.objects.exists():
			return False
		super().save(*args, **kwargs)


	def __str__(self):
		return 'Statistic section'


	class Meta:
		verbose_name_plural = 'Statistic section'


class Statistics(models.Model):
	icon = models.CharField(max_length=200)
	title = models.CharField(max_length=250)
	rank = models.IntegerField(default=0)
	added_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title


	class Meta:
		verbose_name_plural = 'Statistics'


class PortifolioSection(models.Model):
	heading = models.CharField(max_length=250)
	paragraph = models.TextField()
	added_date = models.DateTimeField(auto_now_add=True)


	# This method will avoid to allow more than one instance being saved
	def save(self, *args, **kwargs):
		if not self.pk and PortifolioSection.objects.exists():
			return False
		super().save(*args, **kwargs)


	def __str__(self):
		return self.heading

	class Meta:
		verbose_name_plural = 'Portifolio section'


class Portifolio(models.Model):
	image = models.ImageField(upload_to='images')
	description = models.CharField(max_length=250)
	added_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title


	class Meta:
		verbose_name_plural = 'Portifolio'


class Categories(models.Model):
	category = models.CharField(max_length=250)
	added_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.category


	class Meta:
		verbose_name_plural = 'Categories'


class BlogSection(models.Model):
	head = models.CharField(max_length=250)
	paragraph = models.CharField(max_length=300)
	added_date = models.DateTimeField(auto_now_add=True)


	# This method will avoid to allow more than one instance being saved
	def save(self, *args, **kwargs):
		if not self.pk and BlogSection.objects.exists():
			return False
		super().save(*args, **kwargs)


	def __str__(self):
		return self.head


	class Meta:
		verbose_name_plural = 'Blog section'


class Blogs(models.Model):
	image = models.ImageField(upload_to='images')
	category = models.ForeignKey(Categories, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.TextField()
	author = models.OneToOneField(User, models.CASCADE)
	added_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.author


	class Meta:
		verbose_name_plural = 'Blogs'


class Contact(models.Model):
	location = models.CharField(max_length=250)
	telephone = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	added_date = models.DateTimeField(auto_now_add=True)


	# This method will avoid to allow more than one instance being saved
	def save(self, *args, **kwargs):
		if not self.pk and Contact.objects.exists():
			return False
		super().save(*args, **kwargs)


	def __str__(self):
		return self.location


	class Meta:
		verbose_name_plural = 'Contact'


class SocialMedia(models.Model):
	name = models.CharField(max_length=250)
	icon = models.CharField(max_length=250)
	link = models.URLField()
	added_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.name


	class Meta:
		verbose_name_plural = 'Social media'
