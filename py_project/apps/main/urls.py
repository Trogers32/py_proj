from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView
                    
urlpatterns = [
    url(r'^$', views.home),
    # url(r'^.*$', RedirectView.as_view(url='/', permanent=False), name='index')
]