from faker import Faker
import factory
from unittest.mock import Mock
from datetime import datetime
from django.utils.timezone import make_aware
from .. import models


class BlogEntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BlogEntry

    title = factory.Faker('text', max_nb_chars=100)
    draft = False
    pub_date = make_aware(datetime.now())
    updated = datetime.now()
    content = factory.Faker('paragraphs')
    tags = Mock()
    image = factory.Faker('file_path')
