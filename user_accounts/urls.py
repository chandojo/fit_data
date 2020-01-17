from django.urls import path, include
from .views import BlogAuthorViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'blog-authors', BlogAuthorViewSet, basename='blogauthors')

app_name = 'user_accounts'

urlpatterns = [
    path('api/authors/', include(router.urls)),

]
