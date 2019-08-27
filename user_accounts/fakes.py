import factory

from . import models


class BlogAuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BlogAuthor

    username = factory.Faker('user_name')
