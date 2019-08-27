from django.urls import path, include
from .views import BlogEntryViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'blogentries', BlogEntryViewSet, basename='blogentries')

app_name='blog'

urlpatterns = [
    path('api/blog/', include(router.urls)),
]
