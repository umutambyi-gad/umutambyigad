from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.template.defaultfilters import slugify


# Create your models here.
class Introduction(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	background_image = CloudinaryField('images')
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
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = CloudinaryField('images')
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
	background_image = CloudinaryField('images')
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

	# method to return number for bootstrap col ex. col-lg-{collumns_count}
	@classmethod
	def columns_count(cls):
		if cls.objects.count() > 0:
			return 12 // cls.objects.count()
		return False

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


class Categories(models.Model):
	category = models.CharField(max_length=250)
	added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.category

	class Meta:
		verbose_name_plural = 'Categories'


class Portifolio(models.Model):
	image = CloudinaryField('images')
	description = models.CharField(max_length=250)
	category = models.ForeignKey(Categories, on_delete=models.CASCADE)
	added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.description[:20]

	class Meta:
		verbose_name_plural = 'Portifolio'


class Tags(models.Model):
	name = models.CharField(max_length=250)
	added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Tags'



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
	title = models.CharField(max_length=200)
	thumbnail = CloudinaryField('images')
	category = models.ForeignKey(Categories, on_delete=models.CASCADE)
	short_description = models.TextField()
	content = models.TextField()
	image_1 = CloudinaryField('images', null=True, blank=True)
	image_2 = CloudinaryField('images', null=True, blank=True)
	image_3 = CloudinaryField('images', null=True, blank=True)
	image_4 = CloudinaryField('images', null=True, blank=True)
	image_5 = CloudinaryField('images', null=True, blank=True)
	tags = models.ManyToManyField(Tags)
	author = models.OneToOneField(User, models.CASCADE)
	added_date = models.DateTimeField(auto_now_add=True)

	@classmethod
	def recent_blogs(cls):
		return cls.objects.order_by('-added_date')

	def slug(self):
		return slugify(self.title)

	def get_absolute_url(self):
		return reverse('website:blog-single', args=[str(self.pk), str(self.slug())])

	def __str__(self):
		return self.author.username

	class Meta:
		verbose_name_plural = 'Blogs'


class BlogSingle(models.Model):
	breadcrumb_image = CloudinaryField('images')
	footer_image = CloudinaryField('images')
	added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'Blog single'

	class Meta:
		verbose_name_plural = 'Blog single'


class Contact(models.Model):
	section_background = CloudinaryField('images')
	location = models.CharField(max_length=250)
	telephone = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	short_message = models.TextField()
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


class RootComments(models.Model):
	blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
	commentor_name = models.CharField(max_length=250)
	commentor_email = models.EmailField()
	comment = models.TextField()
	added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.get_full_name()

	class Meta:
		verbose_name_plural = 'Root Comments'


class ReplyComments(models.Model):
	root_comment = models.ForeignKey(RootComments, on_delete=models.CASCADE)
	commentor_name = models.CharField(max_length=250)
	commentor_email = models.EmailField()
	comment = models.TextField()
	added_date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.user.get_full_name()

	class Meta:
		verbose_name_plural = 'Reply Comments'

