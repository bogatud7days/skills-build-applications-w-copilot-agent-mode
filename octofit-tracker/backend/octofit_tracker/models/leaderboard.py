from djongo import models

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    position = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
