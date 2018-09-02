from django.db import models
from django.urls import reverse_lazy


class Level(models.Model):
    title = models.CharField('제목', max_length=50)
    content = models.TextField('내용')
    made_by_user = models.BooleanField('made_by_user', default=False)
    created = models.DateTimeField('created', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('app:level_detail', kwargs={'pk': self.id})


class Problem(models.Model):
    title = models.CharField('문제', max_length=50)
    level = models.ForeignKey('app.Level', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
