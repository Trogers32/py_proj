from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView
                    
urlpatterns = [
    url(r'^$', views.home),
    url(r'^/$', views.home),
    url(r'^/reset$', views.reset),
    url(r'^/answer$', views.answer),
    url(r'^/next$', views.next),
    url(r'^/change$', views.change),
]