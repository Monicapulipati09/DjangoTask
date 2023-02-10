# Create your models here.
from django.conf import settings
from django.db import models


class Articles(models.Model):
    """
    This model has a Char field to store Author name, JSONField title for storing the translated titles, as well as created and updated fields for
    storing the creation and last modification timestamps, respectively.
    """
    Author = models.CharField(max_length=200)
    title = models.JSONField("Article_Title", default=dict)
    created = models.DateTimeField("Created", auto_now_add=True)
    updated = models.DateTimeField("Updated", auto_now=True)

    def __str__(self):
        return self.title.get(settings.LANGUAGE_CODE, 'Title')