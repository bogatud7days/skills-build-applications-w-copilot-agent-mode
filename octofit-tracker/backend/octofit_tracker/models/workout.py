from djongo import models

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=20)
    class Meta:
        db_table = 'workouts'
