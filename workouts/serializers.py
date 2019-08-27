from .models import *
from .views import *
from rest_framework import serializers

class MuscleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Muscle
		fields = ['id', 'name', 'url']

class MuscleGroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MuscleGroup
		fields = ['id', 'name', 'muscles', 'url']

class ExerciseDifficultySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ExerciseDifficulty
		fields = ['id', 'name', 'url']

class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Exercise
		fields = ['id', 'name', 'video_id', 'url']

class MovementSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Movement
		fields = ['id', 'name', 'url', 'agonist_muscle_group']

class MovementPlaneSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MovementPlane
		fields = ['id', 'name', 'url']

class JointTypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = JointType
		fields = ['id', 'name', 'url']

class JointNumberSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = JointNumber
		fields = ['id', 'name', 'url']

class JointSerializer(serializers.ModelSerializer):
	class Meta:
		model = Joint
		fields = ['id', 'name', 'url', 'joint_type']

class ContractionTypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ContractionType
		fields = ['id', 'name', 'url']

class SidesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Sides
		fields = ['id', 'name', 'url']

class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Equipment
		fields = ['id', 'name', 'url']

class WorkoutTypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = WorkoutType
		fields = ['id', 'name', 'url']

class WorkoutDurationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = WorkoutDuration
		fields = ['id', 'weeks', 'url']

class WorkoutFrequencySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = WorkoutFrequency
		fields = ['id', 'days_per_week', 'url']

class WorkoutPhaseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = WorkoutPhase
		fields = ['id', 'name', 'url']

class WorkoutDifficultySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = WorkoutDifficulty
		fields = ['id', 'name', 'url']

class SeasonPlanDurationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SeasonPlanDuration
		fields = ['id', 'name', 'url']

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Activity
		fields = ['id', 'name', 'url']

class SeasonPlanSerializer(serializers.ModelSerializer):
	class Meta:
		model = SeasonPlan
		fields = ['id', 'name', 'activity', 'season_duration']

class WorkoutExercisesSerializer(serializers.ModelSerializer):
	exercise = ExerciseSerializer(many=False)
	class Meta:
		model = WorkoutExercises
		fields = ['id', 'exercise_order', 'exercise', 'url', 'sets', 'reps', 'rest_btwn_sets_sec', 'intensity', 'intensity_percentage']

class WorkoutSerializer(serializers.ModelSerializer):
	workout_difficulty = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
	workout_type = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
	workout_duration = serializers.SlugRelatedField(many=False, read_only=True, slug_field='weeks')
	workout_frequency = serializers.SlugRelatedField(many=False, read_only=True, slug_field='days_per_week')
	workout_phase = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
	season_plan = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
	workout_exercises = WorkoutExercisesSerializer(many=True)

	class Meta:
		model = Workout
		fields=['id', 'image', 'name', 'workout_type', 'workout_duration', 'workout_frequency', 'workout_phase', 'season_plan', 'workout_difficulty', 'workout_exercises', 'description']
