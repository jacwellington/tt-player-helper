from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from form_templates.models import FormTemplate
from form_templates import views

urlpatterns = patterns('',
    url(r'^$', 
		ListView.as_view(
			queryset= FormTemplate.objects.order_by('name'),
			context_object_name='all_form_templates',
			template_name='form_templates/index.html'),
		name='index'),
	url(r'^(?P<form_id>\d+)/$', views.detail, name='detail')
)
