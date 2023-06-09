from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import settings

from university.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("university.urls")),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:   #####
#     urlpatterns = +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = pageNotFound
