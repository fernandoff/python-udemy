from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    review = models.TextField()
    rating = models.IntegerField()
