from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
]

urlpatterns += staticfiles_urlpatterns()
