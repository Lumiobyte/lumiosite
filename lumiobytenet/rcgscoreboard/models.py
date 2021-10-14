from django.db import models

class PlayerScore(models.Model):

    created = models.DateTimeField(auto_now_add = True)
    time = models.FloatField(default = 0)
    username = models.CharField(max_length = 18, default = "Anonymous")
    level = models.PositiveIntegerField(default = 1)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return f'{self.username} got a time of {self.time} seconds on level {self.level}'
