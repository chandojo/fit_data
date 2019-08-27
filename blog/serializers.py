from .models import *
from .views import *
from rest_framework import serializers

class BlogEntrySerializer(serializers.ModelSerializer):
	author = serializers.CharField(source='author.username', read_only=True)

	class Meta:
		model = BlogEntry
		fields = ['slug', 'id', 'title', 'author', 'pub_date', 'updated', 'content', 'image']
