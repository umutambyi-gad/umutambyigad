from django.contrib import admin
from .models import (
	Careers,
	Introduction
)


# Register your models here.
class CarrersAdmin(admin.ModelAdmin):
	list_display = ('career', 'added_date')

admin.site.register(Carrers, CarrersAdmin)


class IntroductionAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		obj.username = request.user
		return super().save_model(request, obj, form, change)

	list_display = ('username', 'added_date')

admin.site.register(Introduction, IntroductionAdmin)
