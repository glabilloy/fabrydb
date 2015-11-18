import re
from django.conf.urls import url, patterns, include
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.template import add_to_builtins
from fabrydb.admin import fadmin

add_to_builtins('avocado.templatetags.avocado_tags')

admin.autodiscover()

urlpatterns = patterns('',
    # Landing Page
    url(r'^$', 'fabry.views.home', name='home'),
    url(r'^$', 'fabrydb.views.landing', name='landing'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),

    # Cilantro Pages
    url(r'^workspace/', TemplateView.as_view(template_name='index.html'), name='workspace'),
    url(r'^query/', TemplateView.as_view(template_name='index.html'), name='query'),
    url(r'^results/', TemplateView.as_view(template_name='index.html'), name='results'),

    # Serrano-compatible Endpoint
    url(r'^api/', include('serrano.urls')),

    # Administrative components
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fadmin/', include(fadmin.urls), name='fadmin'),
)

# if not settings.DEBUG:
urlpatterns += patterns(
    '',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)


# In production, these two locations must be served up statically
urlpatterns += patterns('django.views.static',
    url(r'^{0}(?P<path>.*)$'.format(re.escape(settings.MEDIA_URL.lstrip('/'))), 'serve', {
        'document_root': settings.MEDIA_ROOT
    }),
    url(r'^{0}(?P<path>.*)$'.format(re.escape(settings.STATIC_URL.lstrip('/'))), 'serve', {
        'document_root': settings.STATIC_ROOT
    }),
)
