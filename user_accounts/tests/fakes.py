import factory

from .. import models


class BlogAuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BlogAuthor

    email = factory.Faker('email')
    name = factory.Faker('name')
    bio = factory.Faker('paragraph', nb_sentences=3)
