from django.conf.urls import patterns, url
urlpatterns = patterns('blog.views',
	url(r'^$', 'home'),
	url(r'^truc/$', 'truc'),
	url(r'^chose/$', 'chose'),
	url(r'^machin/$', 'machin'),
	url(r'^foo/$', 'foo'),
	url(r'^bar/$', 'bar'),

)
