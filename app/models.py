from django.db import models
from django.urls import reverse_lazy


class Level(models.Model):
    title = models.CharField('title', max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('app:level_detail', kwargs={'pk': self.id})


class Problem(models.Model):
    title = models.CharField('title', max_length=50)
    level = models.ForeignKey('app.Level', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
