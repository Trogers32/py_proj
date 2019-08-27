from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView
                    
urlpatterns = [
    url(r'^$', views.home),
    url(r'^contact$', views.contact),
    url(r'^reviews$', views.reviews),
    url(r'^.*$', RedirectView.as_view(url='/', permanent=False), name='index'),
]