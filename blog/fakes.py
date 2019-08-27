from faker import Faker
import factory
from unittest.mock import Mock
from datetime import datetime

from . import models


class BlogEntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BlogEntry

    title = factory.Faker('text')
    draft = False
    pub_date = datetime.now()
    updated = datetime.now()
    content = factory.Faker('paragraphs')
    tags = Mock()
    image = factory.Faker('file_path')
