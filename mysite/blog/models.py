from __future__ import unicode_literals

from django.db import models

# Create your models here.

class blogEntry(models.Model):

    name = models.CharField(max_length=220)
    description = models.CharField(max_length=520)


