from django.db import models
from django.urls import reverse

class Post(models.MODEL):
    title = models.CharField(max_length=50, blank=False)
    author = models.CharField(max_length=50, blank=False)
    date(auto) = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=200, blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('creat', kwargs={'pk': self.pk})
        