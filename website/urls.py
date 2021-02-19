from django.urls import path
from .views import HomeView, blog_single


app_name = 'website'

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('blog/<int:blog_id>/<slug:blog_title_slug>', blog_single, name='blog-single')
]
