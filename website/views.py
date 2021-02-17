from django.shortcuts import render
from django.views import View
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
	Contact,
	SocialMedia
)


# Create your views here.
class HomeView(View):
	def get(self, request, *args, **kwargs):
		context = {
		'Intro': Introduction.objects.first(),
		'careers': Careers.objects.all(),
		'profile': Profile.objects.first(),
		'skills': Skills.objects.all(),
		'service_section': ServiceSection.objects.first(),
		'services': Services.objects.all(),
		'stats_sections': StatisticSection.objects.first(),
		'stats': Statistics.objects.all(),
		'portifolio_section': PortifolioSection.objects.first(),
		'portifolios': Portifolio.objects.all(),
		'blog_section': BlogSection.objects.first(),
		'blogs': Blogs.objects.all(),
		'contact': Contact.objects.first(),
		'social_media': SocialMedia.objects.all()
		}
		return render(request, 'index.html', context)


	def post(self, request, *args, **kwargs):
		pass
