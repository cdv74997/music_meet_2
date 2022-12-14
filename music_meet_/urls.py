from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls')),
]
# setting a url and the file path will be this from set the url to getting the file from root
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
