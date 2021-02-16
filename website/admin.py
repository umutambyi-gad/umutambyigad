from django.contrib import admin
from .models import (
	Careers,
	Introduction,
	Profile,
	Skills,
	ServiceSection,
	Sevices,
	Stastics,
	PortifolioSection,
	Portifolio,
	Categories,
	BlogSection,
	Blogs
)


# Register your models here.
class CareersAdmin(admin.ModelAdmin):
	list_display = ('career', 'added_date')
	list_filter = ('added_date', )

admin.site.register(Careers, CareersAdmin)


class IntroductionAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		obj.username = request.user
		return super().save_model(request, obj, form, change)

	list_display = ('username', 'added_date')

admin.site.register(Introduction, IntroductionAdmin)


class ProfileAdmin(admin.ModelAdmin):
	list_display = ('names' , 'added_date')

admin.site.register(Profile, ProfileAdmin)


class SkillsAdmin(admin.ModelAdmin):
	list_display = ('name', 'added_date')

admin.site.register(Skills, SkillsAdmin)


class ServiceSectionAdmin(admin.ModelAdmin):
	list_display = ('heading', 'added_date')

admin.site.register(ServiceSection, ServiceSectionAdmin)


class SevicesAdmin(admin.ModelAdmin):
	list_display = ('title', 'added_date')

admin.site.register(Sevices, SevicesAdmin)


class StasticsAdmin(admin.ModelAdmin):
	list_display = ('title', 'added_date')

admin.site.register(Stastics, StasticsAdmin)


class PortifolioSectionAdmin(admin.ModelAdmin):
	list_display = ('heading', 'added_date')

admin.site.register(PortifolioSection, PortifolioSectionAdmin)


class PortifolioAdmin(admin.ModelAdmin):
	list_display = ('title', 'added_date')

admin.site.register(Portifolio, PortifolioAdmin)


class CategoriesAdmin(admin.ModelAdmin):
	list_display = ('category', 'added_date')

admin.site.register(Categories, CategoriesAdmin)


class BlogSectionAdmin(admin.ModelAdmin):
	list_display = ('head', 'added_date')

admin.site.register(BlogSection, BlogSectionAdmin)


class BlogsAdmin(admin.ModelAdmin):
	fields = ('image', 'title', 'description', 'category')
	list_display = ('title', 'author', 'added_date')


	def save_model(self, request, obj, form, change):
		obj.author = request.user
		super().save_model(request, obj, form, change)

admin.site.register(Blogs, BlogsAdmin)
