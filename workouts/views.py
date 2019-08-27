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

class ExerciseViewSet(viewsets.ModelViewSet):
	queryset = Exercise.objects.all()
	serializer_class = ExerciseSerializer

class MovementViewSet(viewsets.ModelViewSet):
	queryset = Movement.objects.all()
	serializer_class = MovementSerializer

class MovementPlaneViewSet(viewsets.ModelViewSet):
	queryset = MovementPlane.objects.all()
	serializer_class = MovementPlaneSerializer

class JointTypeViewSet(viewsets.ModelViewSet):
	queryset = JointType.objects.all()
	serializer_class = JointTypeSerializer

class JointNumberViewSet(viewsets.ModelViewSet):
	queryset = JointNumber.objects.all()
	serializer_class = JointNumberSerializer

class JointViewSet(viewsets.ModelViewSet):
	queryset = Joint.objects.all()
	serializer_class = JointSerializer

class ContractionTypeViewSet(viewsets.ModelViewSet):
	queryset = ContractionType.objects.all()
	serializer_class = ContractionTypeSerializer

class SidesViewSet(viewsets.ModelViewSet):
	queryset = Sides.objects.all()
	serializer_class = SidesSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
	queryset = Equipment.objects.all()
	serializer_class = EquipmentSerializer

class WorkoutTypeViewSet(viewsets.ModelViewSet):
	queryset = WorkoutType.objects.all()
	serializer_class = WorkoutTypeSerializer

class WorkoutDurationViewSet(viewsets.ModelViewSet):
	queryset = WorkoutDuration.objects.all()
	serializer_class = WorkoutDurationSerializer

class WorkoutFrequencyViewSet(viewsets.ModelViewSet):
	queryset = WorkoutFrequency.objects.all()
	serializer_class = WorkoutFrequencySerializer

class WorkoutPhaseViewSet(viewsets.ModelViewSet):
	queryset = WorkoutPhase.objects.all()
	serializer_class = WorkoutPhaseSerializer

class WorkoutExercisesViewSet(viewsets.ModelViewSet):
	queryset = WorkoutExercises.objects.all()
	serializer_class = WorkoutExercisesSerializer

class SeasonPlanDurationViewSet(viewsets.ModelViewSet):
	queryset = SeasonPlanDuration.objects.all()
	serializer_class = SeasonPlanDurationSerializer

class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
	queryset = Workout.objects.all()
	serializer_class = WorkoutSerializer

class WorkoutDifficultyViewSet(viewsets.ModelViewSet):
	queryset = WorkoutDifficulty.objects.all()
	serializer_class = WorkoutDifficultySerializer
