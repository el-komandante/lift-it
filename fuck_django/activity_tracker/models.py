from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class user(User):
    IMPERIAL = 'imp'
    METRIC = 'met'

    unit_choices = ((IMPERIAL, 'Imperial'), (METRIC, 'Metric'))
    units = models.CharField(
        choices=unit_choices,
        default=IMPERIAL,
        max_length=20,
    )

class Activity(models.Model):
    name = models.CharField(max_length=75)
    time = models.DateTimeField('date and time completed')
    duration = models.FloatField(blank=True)
    distance = models.FloatField(blank=True)
    user = models.ForeignKey(user)
    weight = models.FloatField(blank=True)
    sets = models.IntegerField(blank=True)
    reps = models.IntegerField(blank=True)
