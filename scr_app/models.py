from django.db import models


class City(models.Model):
    name = models.CharField(50)
    slug = models.CharField(50, blank=True)
