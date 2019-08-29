from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
                    
urlpatterns = [
    url(r'^$', views.img_sharing),
    url(r'^uploading_file$', views.uploading_file),
    url(r'^clean_session$', views.clean_session),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)