from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include

from Py1802Adv import settings

urlpatterns = [
                  url('admin/', admin.site.urls),
                  url('upload/', include('apps.upload01.urls')),
                  url('session/', include('apps.session01.urls')),
                  url('form/', include('apps.form01.urls')),
                  url('cache/', include('apps.cache01.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
