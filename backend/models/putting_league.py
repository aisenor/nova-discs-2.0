from django.db import models

from .players import Players


class PuttingLeague(models.Model):
    date = models.DateField()
    player = models.ForeignKey(Players, models.DO_NOTHING)
    score = models.IntegerField()

    class Meta:
        db_table = 'putting_league'
