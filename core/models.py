from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    """
    represents a Category (name, description)
    used in cal.models.Event
    """
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Location(models.Model):
    """
    represents a location(name, description, country)
    used in cal.models.Event
    """
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    acrynym = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.name
