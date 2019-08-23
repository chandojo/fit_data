from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *

class MuscleViewSet(viewsets.ModelViewSet):
	queryset = Muscle.objects.all()
	serializer_class = MuscleSerializer

class MuscleGroupViewSet(viewsets.ModelViewSet):
	queryset = MuscleGroup.objects.all()
	serializer_class = MuscleGroupSerializer

class ExerciseDifficultyViewSet(viewsets.ModelViewSet):
	queryset = ExerciseDifficulty.objects.all()
	serializer_class = ExerciseDifficultySerializer

class MovementViewSet(viewsets.ModelViewSet):
	queryset = Movement.objects.all()
	serializer_class = MovementSerializer
