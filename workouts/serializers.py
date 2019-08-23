from .models import *
from rest_framework import serializers

class MuscleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Muscle
		fields = ['name']
