from django.shortcuts import render
from rest_framework import viewsets, filters, permissions

from .serializers import *
from .models import *


class BlogAuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogAuthor.objects.all()
    serializer_class = BlogAuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']
