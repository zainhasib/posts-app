from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('gallery/', include('gallery.urls')),
    path('machine/', include('machine.urls')),
]

urlpatterns += staticfiles_urlpatterns()
