import uuid 
import factory
from faker import Factory as FakerFactory
from todo import models


fake = FakerFactory.create('en_GB')
fake.seed(13337)

"""
By using DjangoModelFactory, the object is inserted in DB 
when TaskFactory() is mentioned, otherwise you can use factory.Factory
"""


class ReadFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Read

