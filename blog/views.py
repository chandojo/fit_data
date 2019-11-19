from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *

class BlogEntryViewSet(viewsets.ModelViewSet):
	queryset = BlogEntry.objects.order_by('-pub_date')
	serializer_class = BlogEntrySerializer
