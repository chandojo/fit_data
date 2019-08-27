from django.urls import path, include
from .views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'muscles', MuscleViewSet, basename='muscles')
router.register(r'muscle-groups', MuscleGroupViewSet)
router.register(r'exercise-difficulty', ExerciseDifficultyViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'movement', MovementViewSet)
router.register(r'movement-plane', MovementPlaneViewSet)
router.register(r'joint', JointViewSet)
router.register(r'joint-type', JointTypeViewSet)
router.register(r'joint-number', JointNumberViewSet)
router.register(r'contraction-type', ContractionTypeViewSet)
router.register(r'sides', SidesViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'workout-type', WorkoutTypeViewSet)
router.register(r'workout-duration', WorkoutDurationViewSet)
router.register(r'workout-frequency', WorkoutFrequencyViewSet)
router.register(r'workout-phase', WorkoutPhaseViewSet)
router.register(r'workout-exercises', WorkoutExercisesViewSet)
router.register(r'movement-plane', MovementPlaneViewSet)
router.register(r'season-plan-duration', SeasonPlanDurationViewSet)
router.register(r'activity', ActivityViewSet)
router.register(r'workout-difficulty', WorkoutDifficultyViewSet, basename='workout-difficulty')
router.register(r'workouts', WorkoutViewSet, basename='workouts')


app_name='workouts'

urlpatterns = [
    path('api/workouts/', include(router.urls)),
]
