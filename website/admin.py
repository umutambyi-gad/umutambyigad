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
	Categories,
	Portifolio
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


class CategoriesAdmin(admin.ModelAdmin):
	list_display = ('category', 'added_date')

admin.site.register(Categories, CategoriesAdmin)


class PortifolioAdmin(admin.ModelAdmin):
	list_display = ('title', 'added_date')

admin.site.register(Portifolio, PortifolioAdmin)