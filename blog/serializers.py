from .models import *
from .views import *
from user_accounts.serializers import BlogAuthorSerializer
from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class BlogEntrySerializer(TaggitSerializer, serializers.ModelSerializer):
    author = BlogAuthorSerializer(required=True)
    tags = TagListSerializerField()

    class Meta:
        model = BlogEntry
        fields = ['slug', 'id', 'title', 'draft', 'author',
                  'pub_date', 'updated', 'content', 'tags', 'image']
