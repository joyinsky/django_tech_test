# coding: utf8
from django.db import models

from .locations import Location

from apps.utils import create_id


def station_id(): return create_id('station')


class Station(models.Model):
    id = models.CharField(default=station_id, primary_key=True,
                          max_length=30, unique=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} <{}>".format(self.location.name, self.id)

