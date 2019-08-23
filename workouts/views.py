from django.shortcuts import render
from rest_framework import viewsets

from .serializers import MuscleSerializer
from .models import *

class MuscleViewSet(viewsets.ModelViewSet):
	queryset = Muscle.objects.all()
	serializer_class = MuscleSerializer
