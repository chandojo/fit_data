from django.shortcuts import render
from rest_framework import viewsets, filters

from .serializers import *
from .models import *


class BlogEntryViewSet(viewsets.ModelViewSet):
    queryset = BlogEntry.objects.all().order_by('-pub_date')
    serializer_class = BlogEntrySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'tags__name', 'slug']
