from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings

# UNDERNEATH your urlpatterns definition, add the following two lines:


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pollingapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/',include('login.urls',namespace='Login')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^polls/',include('polls.urls',namespace='polls',)),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )