from django.contrib import admin
from .models import (
	Introduction,
	Careers,
	Profile,
	Skills,
	ServiceSection,
	Services,
	StatisticSection,
	Statistics,
	PortifolioSection,
	Portifolio,
	Categories,
	BlogSection,
	Blogs,
	BlogSingle,
	Contact,
	SocialMedia,
	Tags
)


# Register your models here.
class IntroductionAdmin(admin.ModelAdmin):
	# Save authenticated user as an author when author field is not given
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)

	list_display = ('user', 'added_date')

admin.site.register(Introduction, IntroductionAdmin)


class CareersAdmin(admin.ModelAdmin):
	list_display = ('career', 'added_date')
	list_filter = ('added_date', )

admin.site.register(Careers, CareersAdmin)


class ProfileAdmin(admin.ModelAdmin):
	# Save authenticated user as an author when author field is not given
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)

	list_display = ('names' , 'added_date')

admin.site.register(Profile, ProfileAdmin)


class SkillsAdmin(admin.ModelAdmin):
	list_display = ('name', 'added_date')

admin.site.register(Skills, SkillsAdmin)


class ServiceSectionAdmin(admin.ModelAdmin):
	list_display = ('heading', 'added_date')

admin.site.register(ServiceSection, ServiceSectionAdmin)


class ServicesAdmin(admin.ModelAdmin):
	list_display = ('title', 'added_date')

admin.site.register(Services, ServicesAdmin)


admin.site.register(StatisticSection)


class StatisticsAdmin(admin.ModelAdmin):
	list_display = ('title', 'added_date')

admin.site.register(Statistics, StatisticsAdmin)


class PortifolioSectionAdmin(admin.ModelAdmin):
	list_display = ('heading', 'added_date')

admin.site.register(PortifolioSection, PortifolioSectionAdmin)


class PortifolioAdmin(admin.ModelAdmin):
	list_display = ('category', 'added_date')

admin.site.register(Portifolio, PortifolioAdmin)


class CategoriesAdmin(admin.ModelAdmin):
	list_display = ('category', 'added_date')

admin.site.register(Categories, CategoriesAdmin)


class BlogSectionAdmin(admin.ModelAdmin):
	list_display = ('head', 'added_date')

admin.site.register(BlogSection, BlogSectionAdmin)


class BlogsAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'added_date')

	# Save authenticated user as an author when author field is not given
	def save_model(self, request, obj, form, change):
		obj.author = request.user
		super().save_model(request, obj, form, change)

admin.site.register(Blogs, BlogsAdmin)


class ContactAdmin(admin.ModelAdmin):
	list_display = ('location', 'added_date')

admin.site.register(Contact, ContactAdmin)


class SocialMediaAdmin(admin.ModelAdmin):
	list_display = ('name', 'added_date')

admin.site.register(SocialMedia, SocialMediaAdmin)


class TagsAdmin(admin.ModelAdmin):
	list_display = ('name', 'added_date')

admin.site.register(Tags, TagsAdmin)


admin.site.register(BlogSingle)
