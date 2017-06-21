from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.urls import reverse_lazy
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('index'), permanent=False)),
    url(r'^invoice/', include('invoice.urls')),

    url('^accounts/', include('django.contrib.auth.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
