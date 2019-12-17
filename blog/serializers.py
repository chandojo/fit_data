from .models import *
from .views import *

from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class BlogEntrySerializer(TaggitSerializer, serializers.ModelSerializer):
    author = serializers.CharField(source='author.name', read_only=True)
    tags = TagListSerializerField()

    class Meta:
        model = BlogEntry
        fields = ['slug', 'id', 'title', 'draft', 'author',
                  'pub_date', 'updated', 'content', 'tags', 'image']
