from django.db import models
from django.db.models import F

# Create your models here.

class Site_Visitors(models.Model):
    count = models.IntegerField(default=0)

    def increment(self) -> int:
        self.count = F('count') + 1
        self.save()
        self.refresh_from_db()
        return self.count

class Projects(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title

class Certifications(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title

class Work(models.Model):
    title = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title