from django.contrib import admin
from .models import (
	Careers,
	Introduction
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
