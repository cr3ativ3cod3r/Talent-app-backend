from django.db import models


class mybookings(models.Model):
    showID = models.BigAutoField
    showname = models.TextField
    place = models.TextField
    time = models.TimeField
    seats_remaining = models.PositiveIntegerField

    def __str__(self):
        return self.showname