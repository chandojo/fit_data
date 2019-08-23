from .models import *
from .views import *
from rest_framework import serializers

class MuscleSerializer(serializers.HyperlinkedModelSerializer):

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

class MovementSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Movement
		fields = ['id', 'name', 'url']
