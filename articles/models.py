from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    image = models.FileField(
        blank=True, upload_to='static/img/uploads/%Y/%m/%d/')
    text = models.TextField()
    is_published = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
