from django.db import models


class Item(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label

class Site(models.Model):
    url = models.CharField(max_length=255)
    items = models.ManyToManyField('Item')

    def __str__(self):
        return self.url

class Config(models.Model):
    items = models.ManyToManyField('Item')
    site = models.ForeignKey(
        'Site',
        on_delete=models.CASCADE,
    )