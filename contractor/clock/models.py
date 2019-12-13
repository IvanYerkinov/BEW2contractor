from django.db import models


class Clock(models.Model):

    name = models.CharField(max_length=150, default="Clock")

    ticks = models.IntegerField(max_length=100, default=0)

    tocks = models.IntegerField(default=4)

    desc = models.CharField(max_length=300, default="")
