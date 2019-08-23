from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Muscle)
admin.site.register(MuscleGroup)
admin.site.register(ExerciseDifficulty)
admin.site.register(Movement)
admin.site.register(MovementPlane)
admin.site.register(Joint)
admin.site.register(JointType)
admin.site.register(ContractionType)
admin.site.register(JointNumber)
admin.site.register(Sides)
admin.site.register(Equipment)
admin.site.register(Exercise)
admin.site.register(WorkoutExercises)
admin.site.register(WorkoutType)
admin.site.register(WorkoutDuration)
admin.site.register(WorkoutFrequency)
admin.site.register(WorkoutPhase)
admin.site.register(SeasonPlanDuration)
admin.site.register(Activity)
admin.site.register(SeasonPlan)
admin.site.register(WorkoutDifficulty)
admin.site.register(Workout)
