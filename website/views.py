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
	BlogSingle,
	Contact,
	SocialMedia,
	RootComments,
	ReplyComments
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


def blog_single(request, blog_id, blog_title_slug):
	total_comments = RootComments.objects.count() + ReplyComments.objects.count()
	context = {
		'blog': Blogs.objects.get(pk=blog_id),
		'recent_blogs': Blogs.recent_blogs(),
		'blog_single': BlogSingle.objects.first(),
		'total_comments': total_comments
	}
	if request.is_ajax():
		commentor_name = unquote(request.POST.get('commentor_name', None))
		commentor_email = unquote(request.POST.get('commentor_email', None))
		comment = unquote(request.POST.get('comment', None))
		commentor_name = commentor_name.replace(' ', '_')
		reply_id = request.POST.get('reply_id', None)
		is_root = False

		if int(reply_id) == 0:
			root = RootComments.objects.create(
				blog= context['blog'],
				commentor_name=commentor_name,
				commentor_email=commentor_email,
				comment=comment
			)
			root.save()
			is_root = True

			return JsonResponse({
				'status':'OK',
				'is_root': is_root,
				'commentor': root.commentor_name,
				'commentor_avatar': 'default.jpg',
				'date': root.added_date.date(),
				'comment': root.comment,
				'id': root.pk,
				'total_comments': RootComments.objects.count() + ReplyComments.objects.count()
				}, status=200
			)
		else:
			reply = ReplyComments.objects.create(
				root_comment=RootComments.objects.get(pk=reply_id),
				commentor_name=commentor_name,
				commentor_email=commentor_email,
				comment=comment
			)
			reply.save()

			return JsonResponse({
				'status':'OK',
				'is_root': is_root,
				'commentor': reply.commentor_name,
				'date': reply.added_date.date(),
				'comment': reply.comment,
				'id': reply_id,
				'total_comments':  RootComments.objects.count() + ReplyComments.objects.count()
				}, status=200
			)
	return render(request, 'blog-single.html', context)
