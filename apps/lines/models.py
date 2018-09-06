# coding: utf8
from django.db import models

from apps.stations.models import Station

from apps.utils import create_id


def line_id(): return create_id('line')


class Line(models.Model):
    id = models.CharField(default=line_id, primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


def route_id(): return create_id('route')


class Route(models.Model):
    id = models.CharField(default=route_id, primary_key=True,
                          max_length=30, unique=True)
    line = models.ForeignKey(Line, on_delete=models.PROTECT)
    stations = models.ManyToManyField(Station)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} <{}>".format(self.line.name, self.id)

    class Meta:
        ordering = ['-id']