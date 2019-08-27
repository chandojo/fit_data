from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_accounts.urls')),
    path('', include('blog.urls')),
    path('', include('workouts.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
