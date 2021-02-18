from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from urllib.parse import unquote
from django.core.mail import send_mail
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
		'stats_section': StatisticSection.objects.first(),
		'stats': Statistics.objects.all(),
		'col_lg': Statistics.columns_count(),
		'portifolio_section': PortifolioSection.objects.first(),
		'portifolios': Portifolio.objects.all(),
		'blog_section': BlogSection.objects.first(),
		'blogs': Blogs.objects.all(),
		'contact': Contact.objects.first(),
		'social_media': SocialMedia.objects.all()
		}

		return render(request, 'index.html', context)

	def post(self, request, *args, **kwargs):
		if request.is_ajax:
			name = unquote(request.POST['name'])
			from_email = unquote(request.POST['email'])
			subject = unquote(request.POST['subject'])
			message = unquote(request.POST['message'])

			send_mail(
				subject,
				f'{name} sends {message}',
				from_email,
				['umutambyig@gmail.com']
			)

			return JsonResponse({
				'message': 'OK'
				}, status=200
			)
